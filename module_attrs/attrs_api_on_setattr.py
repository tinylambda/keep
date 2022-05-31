import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def checker(instance, attribute, new_value):
    logging.info(instance)
    logging.info(attribute)
    logging.info(new_value)
    logging.info(
        "%s old_value=%s and new_value=%s",
        f"{instance.__class__.__name__}.{attribute.name}",
        getattr(instance, attribute.name),
        new_value,
    )
    if new_value <= 1000:
        raise ValueError("should be greater than 1000")


@attr.s(on_setattr=checker)
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == "__main__":
    c = C(100, 200)
    logging.info("%s", c)

    try:
        c.x = 200
    except ValueError as e:
        logging.warning("error when setting value")

    logging.info("%s", c)
