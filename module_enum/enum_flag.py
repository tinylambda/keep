from enum import Flag


class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64


if __name__ == "__main__":
    first_week_day = Weekday.MONDAY
    print(first_week_day)

    weekend = Weekday.SATURDAY | Weekday.SUNDAY
    print(weekend)

    print(Weekday.MONDAY in weekend)  # False
    print(Weekday.SUNDAY in weekend)  # True
