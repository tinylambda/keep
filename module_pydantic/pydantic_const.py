from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    role = Field(default="user", const=True)
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


if __name__ == "__main__":
    user = User(id=10)
    print(user)

    try:
        user = User(id=11, role="other")
    except ValidationError as e:
        print(e)
