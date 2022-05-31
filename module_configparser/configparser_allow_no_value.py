import configparser


try:
    parser = configparser.ConfigParser()
    parser.read("test5.ini")
except configparser.ParsingError as err:
    print("Could not parse:", err)


# Allow stand-alone option names
print("\nTrying again with allow_no_value=True")
parser = configparser.ConfigParser(allow_no_value=True)
parser.read("test5.ini")

for flag in ["a", "b", "c", "d", "e", "x"]:
    print("\n", flag)
    exists = parser.has_option("flags", flag)
    print("has_option: ", exists)
    if exists:
        print("get: ", parser.get("flags", flag))
