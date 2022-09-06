import pprint

from pydantic import BaseModel, Field


class User(BaseModel):
    f: str = Field(title="Good Field")


if __name__ == "__main__":
    user = User(f="hello")
    print(user)
    pprint.pprint(dir(user))
    print(user.__fields__)
    field_f = user.__fields__["f"]
    pprint.pprint(dir(field_f))
    print(field_f.field_info)

    field_info = field_f.field_info
    print(field_info.title)
