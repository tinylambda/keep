class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    d = Date.__new__(Date)
    print(d)

    try:
        d.year
    except AttributeError as e:
        print(e)

    data = {'year': 2012, 'month': 8, 'day': 29}
    for key, value in data.items():
        setattr(d, key, value)

    print(d.year, d.month)

