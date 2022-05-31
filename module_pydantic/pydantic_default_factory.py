import uuid
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid.uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


if __name__ == "__main__":
    m1 = Model()
    m2 = Model()
    print(m1)
    print(m2)
