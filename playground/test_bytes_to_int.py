filename = '/Users/felix/Downloads/10791705.txt'

with open(filename, 'rb') as f:
    for line in f:
        line = line.strip()
        print(int.from_bytes(line, 'little'))
        print(int(line, 16))

