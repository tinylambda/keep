from typing import Literal

from pydantic import BaseModel, ValidationError


class Pie(BaseModel):
    flavor: Literal['apple', 'pumpkin']


if __name__ == '__main__':
    Pie(flavor='apple')
    Pie(flavor='pumpkin')

    try:
        Pie(flavor='cherry')
    except ValidationError as e:
        print(e)
