from datetime import datetime, timedelta

from pytz import timezone

if __name__ == "__main__":
    print(datetime.utcnow())

    d = datetime(2012, 12, 12, 9, 30, 0)
    print(d)

    # localize the date for Chicago
    central = timezone("US/Central")
    loc_d = central.localize(d)
    print(loc_d)

    bang_d = loc_d.astimezone(timezone("Asia/Kolkata"))
    print(bang_d)

    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)
    print(loc_d)
    later = loc_d + timedelta(minutes=30)
    print(later)

    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)

    d = datetime(2022, 6, 29, 16, 0, 0, tzinfo=timezone("US/Eastern"))

    new_york = timezone("US/Eastern")
    print(new_york)

    new_york_time = d.astimezone(new_york)
    print(new_york_time)

    beijing_time = new_york_time.astimezone(timezone("Asia/Shanghai"))
    print(beijing_time)

    print("More")
    utc_tz_name = "UTC"
    pdt_tz_name = "America/Los_Angeles"

    utc_tz = timezone(utc_tz_name)
    pdt_tz = timezone(pdt_tz_name)

    _utc_now = datetime.utcnow()
    _utc_now = utc_tz.localize(_utc_now)

    pdt_now = _utc_now.astimezone(pdt_tz)
    print(_utc_now)
    print(pdt_now)
    print(pdt_now.strftime("%Y-%m-%d"))
