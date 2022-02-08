from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)

# Set of names of fields which were set when the model instance was initialised
print('__fields_set__: ', user.__fields_set__)

# a dictionary of the model's fields
print('__fields__: ', user.__fields__)

print('__config__: ', user.__config__)

print(user)

print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
