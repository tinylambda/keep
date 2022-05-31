from datetime import datetime

from pydantic import BaseModel, validator


class DemoModel(BaseModel):
    ts: datetime = None

    # You'll often want to use this together with pre, since otherwise with always=True
    # pydantic would try to validate the default None which would cause an error.
    @validator("ts", pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()


if __name__ == "__main__":
    print(DemoModel())
    print(DemoModel(ts="2017-11-08T14:00"))
