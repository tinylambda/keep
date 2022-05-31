from datetime import datetime

from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    a = datetime(2012, 9, 23)
    # a + timedelta(months=1)  # months is an invalid keyword
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    d = relativedelta(b, a)
    print(d.months)
    print(d.days)
