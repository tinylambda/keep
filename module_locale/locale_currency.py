import locale

sample_locales = [
    ("CN", "zh_CN"),
    ("USA", "en_US"),
]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    print(
        "{:>10}: {:>10} {:>10}".format(
            name,
            locale.currency(1234.56),
            locale.currency(-1234.56),
        )
    )
