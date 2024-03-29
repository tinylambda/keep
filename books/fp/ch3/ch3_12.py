DIAL_CODES = [
    (86, "China"),
    (91, "India"),
    (1, "United States"),
    (62, "Indonesia"),
    (55, "Brazil"),
    (92, "Pakistan"),
    (880, "Bangladesh"),
    (234, "Nigeria"),
    (7, "Russia"),
    (81, "Japan"),
]

if __name__ == "__main__":
    d1 = dict(DIAL_CODES)
    print("d1: ", d1.keys())

    d2 = dict(sorted(DIAL_CODES))
    print("d2: ", d2.keys())

    d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
    print("d3: ", d3.keys())

    print(d1 == d2 == d3)
