import logging
import sys

import simple.simple_pb2 as all_types
from simple.simple_pb2 import AbstractData, User, Email


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    data = AbstractData(data_type='User')
    user = User(uid='user001', age=34)

    user_bytes = user.SerializeToString()
    logging.info(user_bytes)

    data.data = user_bytes
    data_bytes = data.SerializeToString()
    logging.info(data_bytes)

    logging.info('-' * 64)

    first_unpack = AbstractData.FromString(data_bytes)
    logging.info('first unpack data_type %s', first_unpack.data_type)

    data_type_obj = getattr(all_types, first_unpack.data_type)
    logging.info('type is %s', data_type_obj)

    if data_type_obj is not None:
        data_obj = data_type_obj.FromString(data.data)
        logging.info('real data object is %s', data_obj)

    data = AbstractData(data_type='Email')
    email = Email(to_uid='user001', from_uid='user002', content='hello, im user_002')
    email_bytes = email.SerializeToString()
    data.data = email_bytes
    data_bytes = data.SerializeToString()
    logging.info('data bytes: %s', data_bytes)

    first_unpack = AbstractData.FromString(data_bytes)
    logging.info('first unpack: %s', first_unpack)
    data_type_obj = getattr(all_types, first_unpack.data_type)
    if data_type_obj is not None:
        data_obj = data_type_obj.FromString(data.data)
        logging.info('real data object is %s', data_obj)
