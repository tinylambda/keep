import csv
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    fieldnames = ['Title 1', 'Title 2', 'Title 3', 'Title 4']
    headers = {n: n for n in fieldnames}

    unicode_chars = '中国人'

    with open(sys.argv[1], 'wt', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(3):
            writer.writerow({
                'Title 1': i + 1,
                'Title 2': chr(ord('a') + i),
                'Title 3': '08/{:02d}/07'.format(i+1),
                'Title 4': unicode_chars[i],
            })

    logging.info('%s', open(sys.argv[1], 'rt').read())
