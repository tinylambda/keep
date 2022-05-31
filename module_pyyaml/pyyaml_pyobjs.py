import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    result = yaml.load(
        """
    none: [~, null]
    bool: [true, false, on, off]
    int: 42
    float: 3.14159
    list: [LITE, RES_ACID, SUS_DEXT]
    dict: {hp: 13, sp: 5}
    """,
        yaml.SafeLoader,
    )
    logging.info("%s", result)
