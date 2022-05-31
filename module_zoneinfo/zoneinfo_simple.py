import logging
import sys
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta, timezone

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == "__main__":
    dt_no_tzinfo = datetime(2020, 10, 31, 12)
    logging.info("dt_no_tzinfo: %s", dt_no_tzinfo)
    logging.info("dt_no_tzinfo tzname: %s", dt_no_tzinfo.tzname())

    dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
    logging.info("dt: %s", dt)
    logging.info("dt tzname: %s", dt.tzname())

    dt_add = dt + timedelta(days=1)
    logging.info("dt_add: %s", dt_add)
    logging.info("dt_add tzname: %s", dt_add.tzname())

    dt = datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
    logging.info("dt no fold: %s", dt)
    logging.info("dt fold: %s", dt.replace(fold=1))

    LOS_ANGELES = ZoneInfo("America/Los_Angeles")
    dt_utc = datetime(2020, 11, 1, 8, tzinfo=timezone.utc)
    logging.info("before PDT to PST: %s", dt_utc.astimezone(LOS_ANGELES))
    logging.info(
        "after PDT to PST: %s", (dt_utc + timedelta(hours=1)).astimezone(LOS_ANGELES)
    )

    zoneinfo_asia_shanghai = ZoneInfo("Asia/Shanghai")
    dt_utc = datetime(2020, 11, 1, 8, tzinfo=timezone.utc)
    dt_asia_shanghai = dt_utc.astimezone(zoneinfo_asia_shanghai)
    logging.info("dt_utc: %s", dt_utc)
    logging.info("dt_asia_shanghai: %s", dt_asia_shanghai)
