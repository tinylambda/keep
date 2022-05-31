from datetime import timedelta
from datetime import datetime

if __name__ == "__main__":
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    print("-" * 64)

    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)

    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    print("-" * 64)

    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print((a - b).days)
