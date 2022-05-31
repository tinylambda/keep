import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    result = yaml.dump(list(range(50)))
    logging.info("%s", result)

    result = yaml.dump(list(range(50)), width=50, indent=4, default_flow_style=True)
    logging.info("%s", result)

    result = yaml.dump(list(range(50)), canonical=True)
    logging.info("%s", result)

    result = yaml.dump(list(range(50)), default_flow_style=False)
    logging.info("%s", result)
