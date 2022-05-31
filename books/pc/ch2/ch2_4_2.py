import re


if __name__ == "__main__":
    text = "yeah, but no, but yeah, but no, but yeah"
    print(text == "yeah")
    print(text.startswith("yeah"))
    print(text.endswith("no"))
    print(text.find("no"))

    text1 = "11/27/2012"
    text2 = "Nov 27, 2012"
    if re.match(r"\d+/\d+/\d+", text1):
        print("yes")
    else:
        print("no")

    if re.match(r"\d+/\d+/\d+", text2):
        print("yes")
    else:
        print("no")

    print("-" * 64)

    datepat = re.compile(r"\d+/\d+/\d+")
    if datepat.match(text1):
        print("yes")
    else:
        print("no")

    if datepat.match(text2):
        print("yes")
    else:
        print("no")

    print("-" * 64)

    text = "today is 11/27/2012 PyCon starts 3/13/2013"
    result = datepat.findall(text)
    print(result)

    print("-" * 64)

    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    m = datepat.match("11/27/2012")
    print(m)

    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
    month, day, year = m.groups()

    print("-" * 64)

    print(text)
    print(datepat.findall(text))
    for month, day, year in datepat.findall(text):
        print("{}-{}-{}".format(year, month, day))

    print("-" * 64)

    for m in datepat.finditer(text):
        print(m)
        print(m.groups())

    print("-" * 64)

    m = datepat.match("11/27/2012abcdef")
    print(m)
    print(m.group())
    for group in m.groups():
        print(group)

    print("-" * 64)

    datepat = re.compile(r"(\d+)/(\d+)/(\d+)$")
    m = datepat.match("11/27/2012abcdef")
    print(m)

    m = datepat.match("11/27/2012")
    print(m)

    print("-" * 64)

    f = re.findall(r"(\d+)/(\d+)/(\d+)", text)
    print(f)
