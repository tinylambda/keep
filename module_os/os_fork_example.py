import os

pid = os.fork()

if pid:
    print(f"Child process id: {pid}")
else:
    print("I am the child")
