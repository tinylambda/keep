import datetime

import dateutil.tz


if __name__ == "__main__":
    localtz = dateutil.tz.gettz("Europe/Paris")
    confusing = datetime.datetime(2017, 10, 29, 2, 30)
    print(localtz.is_ambiguous(confusing))
