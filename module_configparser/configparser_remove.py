import configparser


parser = configparser.ConfigParser()
parser.read("test.ini")

print("Read values:\n")
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print("{} = {!r}".format(name, value))

parser.remove_option("bug_tracker", "url")
parser.remove_section("wiki")

print("\nModified values:\n")
for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print("{} = {!r}".format(name, value))
