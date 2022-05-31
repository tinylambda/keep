import datetime

from dateutil.zoneinfo import get_zonefile_instance
from dateutil import tz

if __name__ == "__main__":
    zones = list(get_zonefile_instance().zones)
    print(sorted(zones)[:5])
    print(len(zones))
    localzone = tz.gettz()

    print(localzone)
    print(localzone.tzname(datetime.datetime(2018, 10, 19)))
    print(localzone.tzname(datetime.datetime(2018, 11, 19)))
