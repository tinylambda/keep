from datetime import datetime

from pydantic import ValidationError
from pydantic.dataclasses import dataclass


class MyConfig:
    max_anystr_length = 10
    validate_assignment = True
    error_msg_templates = {
        'value_error.any_str.max_length': 'max_length: {limit_value}',
    }


@dataclass(config=MyConfig)
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


if __name__ == '__main__':
    user = User(id='47', signup_ts='2022-01-10T14:00:00')
    try:
        user.name = 'x' * 20
    except ValidationError as e:
        print(e)
