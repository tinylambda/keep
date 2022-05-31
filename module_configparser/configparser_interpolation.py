from configparser import ConfigParser

parser = ConfigParser()
parser.read("test8.ini")

print("Original value: ", parser.get("bug_tracker", "url"))

parser.set("bug_tracker", "port", "9090")
print("Altered port value: ", parser.get("bug_tracker", "url"))

print("Without interpolation: ", parser.get("bug_tracker", "url", raw=True))
