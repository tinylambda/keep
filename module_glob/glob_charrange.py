import glob


for name in sorted(glob.glob("../module_arra[a-z]")):
    print(name)
