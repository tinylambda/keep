from __future__ import print_function

import logging
import grpc
import grpc.experimental


protos = grpc.protos("helloworld.proto")
services = grpc.services("helloworld.proto")

response = services.Greeter.SayHello(
    protos.HelloRequest(name="you"), "localhost:50051", insecure=True
)
print(f"greeter client received: {response.message}")
