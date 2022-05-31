from configparser import ConfigParser
import datetime


def parse_iso_datetime(s):
    print("parse_iso_datetime({!r})".format(s))
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f")


parser = ConfigParser(converters={"datetime": parse_iso_datetime})

parser.read("test4.ini")
string_value = parser["datetimes"]["due_date"]
value = parser.getdatetime("datetimes", "due_date")
print("due_date: {!r} -> {!r}".format(string_value, value))
