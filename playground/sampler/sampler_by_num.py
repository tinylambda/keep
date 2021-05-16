import os
import sys
import numbers
import typing


def sample(seed_filename: typing.AnyStr, output_num: numbers.Integral):
    base_with_dir, ext = os.path.splitext(seed_filename)
    base_with_dir += f'-{output_num}'

    count = 0
    output_filename = f'{base_with_dir}' + ext

    with open(seed_filename) as seed_file, open(output_filename, 'w') as output_file:
        while count < output_num:
            try:
                line = next(seed_file)
            except StopIteration:
                seed_file.seek(0)
                continue
            output_file.write(line)
            count += 1

    print(f'output to {output_filename}')


if __name__ == '__main__':
    seed_filename = sys.argv[1]
    scales = [1000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2560000, 5120000, 10240000, 20480000]
    # output_num = int(sys.argv[2])
    # sample(seed_filename, output_num)
    for scale in scales:
        sample(seed_filename, scale)

    print('all done')

