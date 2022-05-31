import random
from datetime import datetime
from typing import ClassVar

from pydantic import BaseModel, PrivateAttr


class TimeAwareModel(BaseModel):
    _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
    _secret_value: str = PrivateAttr()

    def __init__(self, **data):
        super(TimeAwareModel, self).__init__(**data)
        self._secret_value = random.randint(1, 5)


class Model(BaseModel):
    _class_var: ClassVar[str] = "class var value"
    _private_attr: str = "private attr value"

    class Config:
        underscore_attrs_are_private = True


if __name__ == "__main__":
    m = TimeAwareModel()
    print(m._processed_at)
    print(m._secret_value)

    # If Config.underscore_attrs_are_private is True, any non-ClassVar underscore attribute will be treated as private:
    print(Model._class_var)
    print(Model._private_attr)
    print(Model()._private_attr)
