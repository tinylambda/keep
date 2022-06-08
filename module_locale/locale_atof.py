import locale

sample_data = [
    ("CN", "zh_CN", "1,234.56"),
    ("USA", "en_US", "1,234.56"),
]

for name, loc, a in sample_data:
    locale.setlocale(locale.LC_ALL, loc)
    print("{:>10}: {:>9} => {:f}".format(name, a, locale.atof(a)))
