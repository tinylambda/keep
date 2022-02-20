from pydantic import BaseModel, ByteSize


class MyModel(BaseModel):
    size: ByteSize


if __name__ == '__main__':
    print(MyModel(size=52000).size)
    print(MyModel(size='3000 KiB').size)
    print(MyModel(size='50 PB').size.human_readable())
    print(MyModel(size='50 PB').size.human_readable(decimal=True))
    print(MyModel(size='50 PB').size.to('tib'))
