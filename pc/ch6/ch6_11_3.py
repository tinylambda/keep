from collections import namedtuple
from ch6_11_2 import read_records


Record = namedtuple('Record', ['kind', 'x', 'y'])


with open('data.db', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

    for r in records:
        print(r.kind, r.x, r.y)

