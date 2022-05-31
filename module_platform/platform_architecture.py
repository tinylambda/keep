import platform
import sys

if __name__ == "__main__":
    print("sys.executable: ", sys.executable)
    print("interpreter (sys.executable): ", platform.architecture())
    print("/bin/ls: ", platform.architecture("/bin/ls"))
