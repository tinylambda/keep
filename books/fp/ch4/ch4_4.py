import array

if __name__ == "__main__":
    numbers = array.array("h", [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)
