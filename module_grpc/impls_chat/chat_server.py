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
            logging.exception("something bad happened", e)

    def create_task(self, coro):
        current_loop = asyncio.get_event_loop()
        task = current_loop.create_task(coro)
        task.add_done_callback(self.task_callback)
        return task

    async def send_message(self, channel_name, message):
        queues = self.channel_cache[channel_name]
        for queue in queues:
            await queue.put(message)

    async def join_channel(self, channel_name, who):
        if channel_name in self.channel_cache:
            return

        msg_channel = asyncio.Queue()
        self.channel_cache[channel_name].append(msg_channel)
        join_message = f"{who} join channel {channel_name}!"
        await self.send_message(channel_name, join_message)

        while True:
            message = await msg_channel.get()
            yield message

    async def JoinChannel(
        self, request: chat_pb2.Channel, context: grpc.aio.ServicerContext
    ):
        async for message in self.join_channel(request.name, request.senders_name):
            yield message

    async def SendMessage(
        self, request_iterator, context: grpc.aio.ServicerContext
    ) -> chat_pb2.MessageAck:
        async for message in request_iterator:
            self.create_task(self.send_message(message.channel.name, message))
        return chat_pb2.MessageAck(status="OK {}".format(id(self)))


async def serve() -> None:
    server = grpc.aio.server()
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())
