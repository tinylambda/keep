import asyncio
import collections
import logging
import grpc

import chat_pb2
import chat_pb2_grpc


class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self, *args, **kwargs):
        super(ChatServicer, self).__init__(*args, **kwargs)
        self.channel_cache = collections.defaultdict(set)

    async def JoinChannel(self, request: chat_pb2.Channel, context: grpc.aio.ServicerContext):
        print(request)
        print(context)

    async def SendMessage(self, request_iterator, context: grpc.aio.ServicerContext) -> chat_pb2.MessageAck:
        return chat_pb2.MessageAck(status='OK')


async def serve() -> None:
    server = grpc.aio.server()
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())

