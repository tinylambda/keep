import re

from calendar import month_abbr


if __name__ == "__main__":
    text = "yeah, but no, but yeah, but no, but yeah"
    result = text.replace("yeah", "yep")
    print(text)
    print(result)

    print("-" * 64)

    text = "today is 11/27/2012. PyCon starts 3/13/2013"
    result = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
    print(text)
    print(result)

    print("-" * 64)

    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    result = datepat.sub(r"\3-\1-\2", text)
    print(result)

    print("-" * 64)

    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return "{} {} {}".format(m.group(2), mon_name, m.group(3))

    result = datepat.sub(change_date, text)
    print(result)

    print("-" * 64)

    newtext, n = datepat.subn(r"\3-\1-\2", text)
    print(newtext)
    print(n)
