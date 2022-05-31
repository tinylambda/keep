# not elegant
import re

if __name__ == "__main__":
    filename = "spam.txt"
    print(filename[-4:] == ".txt")

    url = "http://www.python.org"
    print(url[:5] == "http:" or url[:6] == "https:" or url[:4] == "ftp:")

    # good one
    result = re.match("http:|https:|ftp:", url)
    print(result)
