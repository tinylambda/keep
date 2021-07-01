import html

s = 'Elements are written as "<tag>text</tag>".'

if __name__ == '__main__':
    print(s)
    print(html.escape(s))
    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    print(
        s.encode('ascii', errors='xmlcharrefreplace')
    )

    from html.parser import HTMLParser
    from html.parser import unescape
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(unescape(s))

    t = 'The prompt is &gt;&gt;&gt;'
    from xml.sax.saxutils import unescape
    print(
        unescape(t)
    )

