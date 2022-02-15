import uuid
from typing import Union
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, str, UUID]
    name: str


class UserAgain(BaseModel):
    id: Union[UUID, int, str]
    name: str


if __name__ == '__main__':
    user_01 = User(id=123, name='John Doe')
    print(user_01)

    user_02 = User(id='1234', name='John Doe')
    print(user_02)

    user_03_uuid = uuid.uuid4()
    user_03 = User(id=user_03_uuid, name='John Doe')
    print(user_03)
    print(user_03.id)
    print(user_03_uuid.int)

    user_03_again = UserAgain(id=user_03_uuid, name='John Doe')
    print(user_03_again)

    user_04 = UserAgain(id=100, name='John Doe')
    print(user_04)
