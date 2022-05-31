import datetime
from dateutil import tz

if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now)

    tz = tz.gettz("Europe/Paris")
    now2 = now.replace(tzinfo=tz)
    print(now2)
