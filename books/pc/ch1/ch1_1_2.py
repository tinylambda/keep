if __name__ == "__main__":
    p = (4, 5)
    x, y = p
    print(x, y)

    data = ["ACME", 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name)
    print(date)

    name, shares, price, (year, month, day) = data
    print(year)
    print(month)
    print(day)

    x, y, z = p  # raise ValueError
