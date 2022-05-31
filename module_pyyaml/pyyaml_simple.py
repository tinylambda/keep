import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    result = yaml.safe_load(
        """
    hello: 中国
    """
    )
    logging.info("%s", result)
