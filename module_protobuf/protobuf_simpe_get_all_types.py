from simple import simple_pb2


if __name__ == "__main__":
    for item in simple_pb2.DESCRIPTOR.message_types_by_name:
        print(item, type(item))
