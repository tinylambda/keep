import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    data = {
        "name": "Felix",
        "race": "human",
        "traits": ["ONE_HAND", "ONE_EYE"],
    }

    result = yaml.dump(data)
    logging.info("%s", result)
