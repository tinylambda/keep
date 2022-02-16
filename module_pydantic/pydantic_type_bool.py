from pydantic import BaseModel, ValidationError


class BoolModel(BaseModel):
    bool_value: bool


if __name__ == '__main__':
    print(BoolModel(bool_value=False))
    print(BoolModel(bool_value='False'))

    try:
        BoolModel(bool_value=[])
    except ValidationError as e:
        print(e)
