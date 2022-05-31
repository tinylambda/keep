from datetime import datetime
from datetime import timedelta

import pytz
from pytz import timezone

if __name__ == "__main__":
    d = datetime(2013, 3, 10, 1, 45)
    print(d)

    # localize the date for Chicago
    central = timezone("US/Central")
    loc_d = central.localize(d)

    print(loc_d)
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)

    later_utc = utc_d + timedelta(minutes=30)
    print(later_utc.astimezone(central))
