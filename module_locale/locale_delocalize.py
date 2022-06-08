import locale

sample_locales = [
    ("CN", "zh_CN"),
    ("USA", "en_US"),
]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    localized = locale.format_string("%0.2f", 123456.78, grouping=True)
    delocalized = locale.delocalize(localized)
    print(
        "{:>10}: {:>10} {:>10}".format(
            name,
            localized,
            delocalized,
        )
    )
