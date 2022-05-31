from configparser import ConfigParser

parser = ConfigParser()
parser.read("test9.ini")

print("URL: ", parser.get("bug_tracker", "url"))
