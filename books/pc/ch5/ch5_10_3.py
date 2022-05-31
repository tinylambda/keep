from ch5_10_2 import memory_map


if __name__ == "__main__":
    m = memory_map("data.bin")
    v = memoryview(m).cast("I")  # memory view of unsigned integers
    v[0] = 7
    print(m[:4])
    m[0:4] = b"\x07\x01\x00\x00"
    print(v[0])
