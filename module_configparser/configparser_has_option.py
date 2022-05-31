from configparser import ConfigParser


parser = ConfigParser()
parser.read("test.ini")

SECTIONS = ["wiki", "none"]
OPTIONS = ["username", "password", "url", "description"]

for section in SECTIONS:
    has_section = parser.has_section(section)
    print("{} section exists: {}".format(section, has_section))
    for candidate in OPTIONS:
        has_option = parser.has_option(section, candidate)
        print("{}.{:<12}: {}".format(section, candidate, has_option))
    print()
