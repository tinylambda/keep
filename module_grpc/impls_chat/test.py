from chat_pb2 import Message
from chat_pb2 import Channel
from google.protobuf.json_format import MessageToJson, MessageToDict
from google.protobuf.json_format import ParseDict


if __name__ == '__main__':
    channel = Channel(name='channel_name', senders_name='felix')
    message = Message(sender='felix', channel=channel, message='content message')

    d1 = MessageToDict(message)
    d1['xxxxx'] = 12334
    print(d1)

    m1 = Message()
    print('before', m1, '!!!')
    ParseDict(d1, m1, ignore_unknown_fields=True)
    print('after', m1, '!!!')


