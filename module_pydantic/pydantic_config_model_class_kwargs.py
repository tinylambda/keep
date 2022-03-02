from pydantic import BaseModel, Extra, ValidationError


class Model(BaseModel, extra=Extra.forbid):
    a: str


if __name__ == '__main__':
    try:
        Model(a='spam', b='extra')
    except ValidationError as e:
        print(e)
