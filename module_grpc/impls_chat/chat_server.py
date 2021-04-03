import chat_pb2
import chat_pb2_grpc


class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def JoinChannel(self, request, context):
        pass

    def SendMessage(self, request_iterator, context):
        pass


