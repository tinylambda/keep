from typing import Any, Optional
from xml.etree.ElementTree import fromstring

from pydantic import BaseModel
from pydantic.utils import GetterDict

xmlstring = """
<User Id="1234">
    <FirstName />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):
    def get(self, key: Any, default: Any = None) -> Any:
        if key in {"Id", "Status"}:
            return self._obj.attrib.get(key, default)
        else:
            try:
                return self._obj.find(key).attrib["Value"]
            except (AttributeError, KeyError):
                return default


class User(BaseModel):
    Id: int
    Status: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter


user = User.from_orm(fromstring(xmlstring))
print(user)
