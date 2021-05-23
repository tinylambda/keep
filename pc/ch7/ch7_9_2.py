from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


if __name__ == '__main__':
    yahoo = UrlTemplate('https://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo.open(names='IBM,APPL,FB', fields='s11c1v'):
        print(line.decode('utf-8'))





