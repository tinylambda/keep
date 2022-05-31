import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    result = yaml.load_all(open("tables.yaml"), yaml.FullLoader)
    logging.info("%s", result)

    for item in result:
        logging.info("%s", item)
