from module_protobuf.game.game_pb2 import Chat_msg


if __name__ == '__main__':
    cm = Chat_msg()
    cm.content = 'abc'
    cm.id = 88899
    cm.ts = '67653846'
    cm.type = 5
    print(dir(cm))
    serialized_bytes = cm.SerializeToString()

    deserialized_object = cm.FromString(serialized_bytes)
    print(deserialized_object)
    print('-' * 64)
    print(deserialized_object.content)


