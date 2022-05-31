from operator import itemgetter


rows = [
    {"fname": "Brian", "lname": "Johns", "uid": 1003},
    {"fname": "David", "lname": "Beazly", "uid": 1002},
    {"fname": "John", "lname": "Cleeze", "uid": 1001},
    {"fname": "Big", "lname": "Johns", "uid": 1004},
]

if __name__ == "__main__":
    rows_by_fname = sorted(rows, key=itemgetter("fname"))
    rows_by_uid = sorted(rows, key=itemgetter("uid"))

    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter("lname", "fname"))
    print(rows_by_lfname)
