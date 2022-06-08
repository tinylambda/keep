import locale
import time

sample_locales = [
    ("CN", "zh_CN"),
    ("USA", "en_US"),
]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    _format = locale.nl_langinfo(locale.D_T_FMT)
    print("{:>10}: {}".format(name, time.strftime(_format)))
