from configparser import ConfigParser
import glob

parser = ConfigParser()
candidates = ["test.ini", "test2.ini", "not_exists.ini"]

found = parser.read(candidates)
missing = set(candidates) - set(found)

print("Found config files: ", sorted(found))
print("Missing files: ", sorted(missing))
