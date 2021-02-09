from module_protobuf.chat.chat_pb2 import MessageText
from module_protobuf.chat.chat_pb2 import MessageType
from module_protobuf.chat.chat_pb2 import ChatMessage

from google.protobuf.json_format import MessageToJson


if __name__ == '__main__':
    cm = ChatMessage()

    tm = MessageText()
    tm.id = '1001'
    tm.ts = '234343'
    tm.template = 'abcd/def'
    tm.content = 'hello'

    print(tm.SerializeToString())
    print(tm)
    print(
        MessageToJson(tm)
    )





