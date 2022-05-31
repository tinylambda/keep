import re


if __name__ == "__main__":
    s = " hello    world    \n"
    s = s.strip()
    print(s)

    print(s.replace(" ", ""))
    print(re.sub(r"\s+", " ", s))
