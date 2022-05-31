from configparser import ConfigParser


parser = ConfigParser()
parser.read("test.ini")

for section_name in parser.sections():
    print("Section: ", section_name)
    section = parser[section_name]
    print("Options: ", list(section.keys()))
    for name in section:
        print("{} = {}".format(name, section[name]))
    print()
