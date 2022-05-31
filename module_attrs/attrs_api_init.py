import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(init=True)
class WithInit:
    x = attr.ib()
    y = attr.ib()

    def __attrs_post_init__(self):
        logging.info("WithInit __attrs_post_init__")


@attr.s(init=False)
class WithoutInit:
    x = attr.ib()
    y = attr.ib()


@attr.s(init=False)
class CustomInit:
    x = attr.ib()
    y = attr.ib()

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


if __name__ == "__main__":
    with_init = WithInit(100, 200)
    logging.info("%s", with_init)

    # without_init = WithoutInit(100, 200)  # not works
    without_init = WithoutInit()
    without_init.x = 100
    without_init.y = 200
    logging.info("%s", without_init)

    custom_init = CustomInit(100, 200)
    logging.info("%s", custom_init)
