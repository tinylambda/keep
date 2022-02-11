from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    a: int
    b = 2
    c: int = 1
    d = 0
    e: float


if __name__ == '__main__':
    print(Model.__fields__)
    print(Model.__fields__.keys())

    m = Model(e=300, a=100)
    print(m.dict())

    try:
        Model(a='x', b='x', c='x', d='x', e='x')
    except ValidationError as e:
        error_locations = [e['loc'] for e in e.errors()]
    # order will be reserved
    print(error_locations)
