import os
import time

print(os.path.exists("/etc/passwd"))
print(os.path.exists("/tmp/spam"))

print(os.path.isfile("/etc/passwd"))
print(os.path.isdir("/etc/passwd"))

print(os.path.islink("/Users/Felix/PycharmProjects/keep/venv/bin/python"))
print(os.path.relpath("/Users/Felix/PycharmProjects/keep/venv/bin/python"))

print(os.path.getsize("/etc/passwd"))
print(os.path.getmtime("/etc/passwd"))

print(time.ctime(os.path.getmtime("/etc/passwd")))

print(os.path.getsize("/Users/Guest/Downloads/x"))  # Permission denied
