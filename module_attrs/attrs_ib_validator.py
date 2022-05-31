import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def validator_1(instance, attribute, passed_value):
    logging.info("%s, %s, %s", instance, attribute, passed_value)
    if passed_value < 0:
        raise ValueError("init value should be greater or equal to 0")


# callable that is called by attrs-generated __init__ methods after the instance has been initialized.
# They receive the initialized instance, the Attribute, and the passed value.
@attr.s
class C:
    x = attr.ib(
        type=int, default=0, validator=[attr.validators.instance_of(int), validator_1]
    )


if __name__ == "__main__":
    c = C(87)
    logging.info("%s", c)

    try:
        c = C(-1)
    except ValueError as e:
        logging.error("error", exc_info=e)
