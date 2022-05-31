import glob


print("Named explicitly: ")
for name in sorted(glob.glob("../module_asyncio/*")):
    print("    {}".format(name))

print("Named with wildcard: ")
for name in sorted(glob.glob("../*/*")):
    print("    {}".format(name))
