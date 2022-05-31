import pathlib


p = pathlib.PurePosixPath("/usr/local/lib")
print("parents: {}".format(p.parent))

print("\nhierarchy: ")
for up in p.parents:
    print(up)
