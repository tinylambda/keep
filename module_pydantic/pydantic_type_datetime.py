from datetime import date, datetime, time, timedelta

from pydantic import BaseModel


class Model(BaseModel):
    d: date = None
    dt: datetime = None
    t: time = None
    td: timedelta = None


if __name__ == '__main__':
    # support seconds and milliseconds
    m = Model(d=1644993047.3116837)
    print(m)
    m = Model(d=1644993047311.6837)
    print(m)

    m = Model(
        d=1644993047.3116837,
        dt='2099-04-23T10:20:30.400+02:30',
        t=time(4, 8, 6),
        td='P3DT12H30M5S',
    )
    print(m)
    print(m.td.days, m.td.seconds)
