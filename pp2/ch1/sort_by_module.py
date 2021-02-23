import time

from pp2.ch1.bytemap_sort import sample_file_name


if __name__ == '__main__':
    items = []
    with open(sample_file_name, 'rt') as f:
        for line in f:
            items.append(int(line))

    # items.sort()
    start = time.perf_counter()
    sorted_items = sorted(items)
    print('Cost: ', time.perf_counter() - start)

