import logging
import sys
import typing

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(auto_attribs=True)
class AutoC:
    cls_var: typing.ClassVar[int] = 5  # this one is ignored
    l: typing.List[int] = attr.Factory(list)
    x: int = 1
    foo: str = attr.ib(default='every attrib needs a type if auto_attribs=True')
    bar: typing.Any = None


if __name__ == '__main__':
    logging.info('%s', attr.fields(AutoC).l.type)
    logging.info('%s', attr.fields(AutoC).x.type)
    logging.info('%s', attr.fields(AutoC).foo.type)
    logging.info('%s', attr.fields(AutoC).bar.type)

    auto_c = AutoC()
    logging.info('%s', auto_c)
    logging.info('%s', AutoC.cls_var)
