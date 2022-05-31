import time
from io import TextIOWrapper


if __name__ == "__main__":
    import sys

    sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding="utf-8", write_through=True)

    for i in range(10):
        print(f"hello {i}")
        time.sleep(1)
