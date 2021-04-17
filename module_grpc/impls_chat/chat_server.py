import asyncio
import collections
import logging
import time
import grpc

import chat_pb2
import chat_pb2_grpc


class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self, *args, **kwargs):
        super(ChatServicer, self).__init__(*args, **kwargs)
        self.channel_cache = collections.defaultdict(list)
        self.join_channel_tasks = []

    @staticmethod
    def task_callback(task):
        try:
            task.result()
        except asyncio.CancelledError:
            pass
        except Exception as e:
            logging.exception('something bad happened', e)

    def create_task(self, coro):
        current_loop = asyncio.get_event_loop()
        task = current_loop.create_task(coro)
        task.add_done_callback(self.task_callback)
        return task

    async def send_message(self, channel_name, message):
        queues = self.channel_cache[channel_name]
        for queue in queues:
            await queue.put(message)

    async def JoinChannel(self, request: chat_pb2.Channel, context: grpc.aio.ServicerContext):
        msg_channel = asyncio.Queue()
        self.channel_cache[request.name].append(msg_channel)
        channel = chat_pb2.Channel(name='ch1', senders_name='go')

        try:
            print(dir(context))
            while True:
                print('kickoff', context.peer())
                message = chat_pb2.Message(
                    sender='go', message='hello from server {}/{}'.format(time.time(), id(self.channel_cache)),
                    channel=channel
                )
                yield message
                await asyncio.sleep(1)
        finally:
            import traceback
            print(''.join(traceback.format_stack()))
            print('I am going to cleanup')

    async def SendMessage(self, request_iterator, context: grpc.aio.ServicerContext) -> chat_pb2.MessageAck:
        async for message in request_iterator:
            self.create_task(self.send_message(message.channel.name, message))
        return chat_pb2.MessageAck(status='OK {}'.format(id(self)))


async def serve() -> None:
    server = grpc.aio.server()
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    def exception_handler(my_loop, context):
        print('get exception...', context)

    def done_callback(task: asyncio.Task):
        try:
            print(task)
            print(task.exception())
            print(task.result())
            result = task.result()
        except asyncio.CancelledError:
            print('get cancelling error, skip')
        except Exception as e:
            print('exception', e)
        else:
            print('every thing goes well: ', result)

    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()

    loop.set_exception_handler(exception_handler)
    original_create_task = loop.create_task

    def mycreate_task(coro):
        task = original_create_task(coro)
        # task.set_name(name)
        task.add_done_callback(done_callback)
        return task

    loop.create_task = mycreate_task
    print(loop.create_task)

    loop.run_until_complete(serve())

