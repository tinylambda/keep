import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(
        validator=attr.validators.deep_mapping(
            key_validator=attr.validators.instance_of(str),
            value_validator=attr.validators.instance_of(int),
            mapping_validator=attr.validators.instance_of(dict),
        )
    )


if __name__ == "__main__":
    c = C(x={"a": 1, "b": 2})
    logging.info("1. %s", c)

    try:
        c = C(None)
    except TypeError as e:
        logging.error("type error", exc_info=e)

    try:
        c = C({"a": 1, 2: 3})
    except TypeError as e:
        logging.error("type error", exc_info=e)
