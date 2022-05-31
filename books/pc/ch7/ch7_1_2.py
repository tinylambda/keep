import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = "".join(keyvals)
    element = f"<{name}{attr_str}>{html.escape(value)}</{name}>"
    return element


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    print(avg(1, 2))
    print(avg(1, 2, 3, 4))

    print(make_element("item", "Albatross", size="large", quantity=6))

    print(make_element("p", "<spam>"))
