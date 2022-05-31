import pathlib
import time


p = pathlib.Path("example_dir")

if not p.exists():
    print("Creating example_dir")
    p.mkdir()

time.sleep(5)

print("Removing {}".format(p))
p.rmdir()
