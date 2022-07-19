import glob
import gzip
import json
import os.path
from datetime import datetime

datapath = "/Users/Felix/Downloads/DataFix/"

for item in glob.glob("/Users/Felix/Downloads/DataFix/*.gz"):
    if "_fixed" in item:
        continue
    f, ext = os.path.splitext(item)
    to_file = f"{f}_fixed{ext}"
    if os.path.exists(to_file):
        print("fixed file exists, continue")
        continue
    print("processing: ", item, f"\nto\n{to_file}")
    with gzip.open(item, "r") as f, gzip.open(to_file, "wb") as tof:
        for line in f:
            items = line.split(b"\t")
            j = items[3]
            d = json.loads(j)
            request_time = d["context"]["request_time"]
            response_time = d["context"]["response_time"]
            delta_milli = d["context"]["time_cost_milliseconds"]

            request_time = datetime.fromisoformat(request_time)
            response_time = datetime.fromisoformat(response_time)
            real_milli = (response_time - request_time).total_seconds() * 1000
            real_milli = round(real_milli, 3)
            if real_milli >= 1000:
                print(request_time, response_time, delta_milli, real_milli)
                d["context"]["time_cost_milliseconds"] = real_milli
                new_j = json.dumps(d)
                items[3] = new_j.encode()
                line = b"\t".join(items)

            tof.write(line)
