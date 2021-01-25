from module_protobuf.game.game_pb2 import Chat_msg


if __name__ == '__main__':
    m = {
        b'2004': Chat_msg,
    }
    cm = Chat_msg()
    cm.content = 'abc'
    cm.id = 88899
    cm.ts = '67653846'
    cm.type = 5
    print(dir(cm))
    serialized_bytes = cm.SerializeToString()
    print(serialized_bytes)

    deserialized_object = cm.FromString(serialized_bytes)
    print(deserialized_object)
    print('-' * 64)
    print(deserialized_object.content)

    your_msg = b'2004' + serialized_bytes
    _type = your_msg[:4]
    _msg = your_msg[4:]

    print('+' * 100)
    print(_type, _msg)
    _obj = m[_type].FromString(_msg)
    print(_obj.type)


