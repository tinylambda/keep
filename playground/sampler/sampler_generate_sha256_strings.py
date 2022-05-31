import sys
import hashlib


if __name__ == "__main__":
    inputs = sys.argv[1:]
    for item in inputs:
        item = item.strip()
        item_bytes = item.encode("utf-8")
        result = hashlib.sha256(item_bytes).hexdigest()
        print(result)
