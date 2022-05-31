import os
import time

if __name__ == "__main__":
    print("Calling...")
    os.system("date;(sleep 3; date)&")

    print("Sleeping")
    time.sleep(5)
