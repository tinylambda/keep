if __name__ == '__main__':
    data = {
        'IMEI': (1.7, 111800),
        'IDFA': (23, 665024),
        'IMEI_MD5': (4.3, 135755),
        'IDFA_MD5': (6.6, 210663),
        'MOBILE_MD5': (29, 914147),
        'USER_ID': (1.8, 181488),
        'OAID': (95, 2237481),
        'OAID_MD5': (58, 1831888),
        'MOBILE_SHA256': (76, 1231734),
    }

    base = 1000
    for k in data:
        v = data[k]
        lines_of_base = int(base / v[0] * v[1])
        print(f'{k} of {base}MB line count is {lines_of_base}')
