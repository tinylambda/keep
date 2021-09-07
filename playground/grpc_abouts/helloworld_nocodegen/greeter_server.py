from concurrent import futures
import logging

import grpc

protos, services = grpc.protos_and_services("helloworld.proto")


class Greeter(services.GreeterServicer):

    def SayHello(self, request, context):
        return protos.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
