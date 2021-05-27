import os
import sys
import numbers
import typing
import json
import random


def sample(seed_filename: typing.AnyStr, output_num: numbers.Integral, format_func=None):
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
            if format_func:
                line = format_func(line)
            output_file.write(line + '\n')
            count += 1

    print(f'output to {output_filename}')


if __name__ == '__main__':
    seed_filename = sys.argv[1]
    scales = [1000, 10000, 20000, 40000, 80000, 160000, 320000]
    # output_num = int(sys.argv[2])
    # sample(seed_filename, output_num)

    def f(line):
        line = line.strip()
        return json.dumps({'id_string': line, 'pay_level': random.randint(0, 3)})

    for scale in scales:
        sample(seed_filename, scale, format_func=f)

    print('all done')

