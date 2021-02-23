import array
import copy
import os
import random
import time

max_records = 10000000
sample_file_name = 'sample.bin'
sample_sorted_file_name = 'sorted_sample.bin'

if __name__ == '__main__':
    # prepare the input file
    sorted_ints = []
    shuffled_ints = None
    if not os.path.exists(sample_file_name):
        for i in range(max_records):
            if random.random() <= 0.9:
                sorted_ints.append(i)

        shuffled_ints = copy.copy(sorted_ints)  # keep sorted_ints
        random.shuffle(shuffled_ints)  # shuffle inplace

        with open(sample_sorted_file_name, 'wt') as f:
            for item in sorted_ints:
                f.write(f'{item}\n')

        with open(sample_file_name, 'wt') as f:
            for item in shuffled_ints:
                f.write(f'{item}\n')

    sorted_ints = []
    with open(sample_sorted_file_name, 'rt') as f:
        for line in f:
            value = int(line)
            sorted_ints.append(value)

    bit_map = bytearray(max_records)
    with open(sample_file_name, 'rt') as f:
        for line in f:
            index = int(line)
            bit_map[index] = 1

    start = time.perf_counter()
    new_sorted_ints = []
    for i in range(max_records):
        bit_value = bit_map[i]
        if bit_value == 1:
            new_sorted_ints.append(i)

    print('Cost: ', time.perf_counter() - start)

    print(len(sorted_ints))
    print(len(new_sorted_ints))

    print(sorted_ints[:100])
    print(new_sorted_ints[:100])

    print(sorted_ints == new_sorted_ints)

