import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls) -> "Date":
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


if __name__ == "__main__":
    today: Date = Date.today()
    print(today.year)
    print(today.month)
    print(today.day)
