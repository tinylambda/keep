import configparser


parser = configparser.ConfigParser()

parser.add_section("bug_tracker")
parser.set("bug_tracker", "url", "http://localhost:8080/bugs")
parser.set("bug_tracker", "username", "felix")
parser.set("bug_tracker", "password", "password")

for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print("{} = {!r}".format(name, value))
