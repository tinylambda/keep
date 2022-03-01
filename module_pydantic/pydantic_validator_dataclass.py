from datetime import datetime

from pydantic import validator
from pydantic.dataclasses import dataclass


@dataclass
class DemoDataClass:
    ts: datetime = None

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()


if __name__ == '__main__':
    print(DemoDataClass())
    print(DemoDataClass(ts='2022-11-12T14:00'))
