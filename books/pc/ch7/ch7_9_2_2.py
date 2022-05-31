from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


if __name__ == "__main__":
    yahoo = urltemplate("https://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
    for line in yahoo(names="IBM,APPL,FB", fields="s11c1v"):
        print(line.decode("utf-8"))
