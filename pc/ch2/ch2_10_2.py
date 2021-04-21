import re


if __name__ == '__main__':
    num = re.compile(r'\d+')
    print(
        num.match('123')
    )

    print(
        num.match('\u0661\u0662\u0663')
    )

    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

    pat = re.compile(r'stra\u00dfe', re.IGNORECASE)
    s = 'stra 纪'
    print(
        pat.match(s)
    )

    print(
        pat.match(s.upper())
    )

    print(s.upper())

