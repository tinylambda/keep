import os
import shutil


path = os.pathsep.join(
    [
        ".",
        os.path.expanduser("~/pymotw"),
    ]
)

mode = os.F_OK | os.R_OK

# There is still a race condition searching for readable files this way, because in the time between finding the file
# and actually trying to use it, the file can be deleted or its permissions can be changed.
filename = shutil.which("config.ini", mode=mode, path=path)

print(filename)
