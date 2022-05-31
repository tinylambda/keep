from urllib.request import urlopen
import csv


def urlprint(protocol, host, domain):
    url = f"{protocol}://{host}.{domain}"
    print(url, end="")


def func0():
    print("I am the real func0")


def func1():
    print("I am the real func")


def func2(arg):
    print("I am the real func2", arg)


def dowprices():
    u = urlopen("http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1")
    lines = (line.decode("utf-8") for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices
