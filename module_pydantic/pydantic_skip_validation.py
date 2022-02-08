from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int
    name: str = 'John Doe'


original_user = User(id=123, age=32)
user_data = original_user.dict()
print(user_data)
fields_set = original_user.__fields_set__
print(fields_set)

new_user = User.construct(_fields_set=fields_set, **user_data)
print(repr(new_user))
print(new_user.__fields_set__)

bad_user = User.construct(id='dog')
print(repr(bad_user))
