import glob


for name in sorted(glob.glob("../*")):
    print(name)
