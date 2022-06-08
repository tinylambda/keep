import locale

sample_locales = [
    ("CN", "zh_CN"),
    ("USA", "en_US"),
]
print("{:>10} {:>10} {:>15}".format("Locale", "Integer", "Float"))
for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print("{:>10}".format(name), end=" ")
    print(locale.format_string("%10d", 123456, grouping=True), end=" ")
    print(locale.format_string("%15.2f", 123456.78, grouping=True))
