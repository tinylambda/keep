import iso8601
import datetime
from dateutil import tz


if __name__ == '__main__':
    now = datetime.datetime.utcnow()
    print(now.isoformat())

    parsed = iso8601.parse_date(now.isoformat())
    print(parsed)

    print(parsed == now.replace(tzinfo=tz.tzutc()))
