import datetime
from dateutil import tz


def utcnow():
    return datetime.datetime.now(tz=tz.tzutc())


if __name__ == '__main__':
    print(utcnow())
    print(utcnow().isoformat())
