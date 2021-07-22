import dateutil.tz
import datetime

if __name__ == '__main__':
    localtz = dateutil.tz.gettz('Europe/Paris')
    utc = dateutil.tz.tzutc()
    confusing = datetime.datetime(2017, 10, 29, 2, 30, tzinfo=localtz)

    print(confusing.replace(fold=0).astimezone(utc))
    print(confusing.replace(fold=1).astimezone(utc))
