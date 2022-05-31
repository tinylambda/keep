import asyncio

import grpc.aio

import helloworld_pb2_grpc
import helloworld_pb2


async def run():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
        print("greeter client received: ", response.message)
        response = await stub.SayHelloAgain(helloworld_pb2.HelloRequest(name="you"))
        print("greeter client received: ", response.message)


if __name__ == "__main__":
    asyncio.run(run())
