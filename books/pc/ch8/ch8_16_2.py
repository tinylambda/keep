import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class NewDate(Date):
    pass


if __name__ == '__main__':
    today = Date.today()
    new_today = NewDate.today()
