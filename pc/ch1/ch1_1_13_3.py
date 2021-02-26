from operator import itemgetter

from pc.ch1.ch1_1_13_2 import rows

if __name__ == '__main__':
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
    print(rows_by_fname)
    print(rows_by_lfname)

    print(min(rows, key=itemgetter('uid')))
    print(max(rows, key=itemgetter('uid')))

