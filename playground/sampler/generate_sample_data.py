import json
import hashlib
import random

filename = "/tmp/sample_data.log"

current = 15210417777
size = 1000000

with open(filename, "w") as f:
    i = 0
    while i < size:
        new_data = {
            "id_string": hashlib.md5(str(current).encode()).hexdigest(),
            "pay_level": random.randint(0, 3),
        }
        new_data_json = json.dumps(new_data)
        f.write(new_data_json + "\n")
        current += 1
        i += 1
