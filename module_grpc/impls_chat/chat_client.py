import asyncio
import logging
import sys

import grpc

import chat_pb2
import chat_pb2_grpc


class ChatClient:
    def __init__(self, host='127.0.0.1', port=50051):
        self.channel = None
        self.stub = None
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()
        self.input_q = asyncio.Queue()

    def create_task(self, coro, name=None):
        def _handle_task_result(completed_task: asyncio.Task):
            try:
                task.result()
            except asyncio.CancelledError:
                pass
            except Exception as e:
                logging.exception('Exception raised by task = %r', completed_task)
        task = self.loop.create_task(coro)
        task.set_name(name)
        task.add_done_callback(_handle_task_result)
        return task

    def get_stdin_input(self):
        asyncio.ensure_future(self.input_q.put(sys.stdin.readline()))

    async def start(self):
        self.loop.add_reader(sys.stdin, self.get_stdin_input)
        # The channel to listen for the message stream
        self.channel = grpc.aio.insecure_channel(f'{self.host}:{self.port}')
        self.stub = chat_pb2_grpc.ChatServiceStub(channel=self.channel)
        task_creation_callables = [
            lambda: self.create_task(self.input_q.get(), 'user_input'),
        ]

        tasks = [f() for f in task_creation_callables]
        while True:
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for i, task in enumerate(tasks):
                task_name = task.get_name()
                if task.done():
                    if task_name == 'user_input':
                        user_input = task.result().strip()
                        logging.info(f'got user input -> {user_input}')

                        action, *remaining = user_input.split('|')
                        if action == 'send':
                            channel_name, senders_name, message = remaining
                            channel = chat_pb2.Channel(name=channel_name, senders_name=senders_name)
                            message = chat_pb2.Message(sender=senders_name, message=message, channel=channel)
                            messages = [message]
                            ack = await self.stub.SendMessage(messages)
                            logging.info(f'got server ack => {ack.status}')
                        elif action == 'join':
                            channel_name, senders_name = remaining
                            channel = chat_pb2.Channel(name=channel_name, senders_name=senders_name)
                            responses = self.stub.JoinChannel(channel)
                            async for response in responses:
                                print(response)
                    else:
                        pass
                    tasks[i] = task_creation_callables[i]()

    async def stop(self):
        print('stopping')
        await self.channel.close()
        print('stopped')


async def serve():
    chat_client = ChatClient()
    await chat_client.start()
    await chat_client.stop()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())
    loop.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()


