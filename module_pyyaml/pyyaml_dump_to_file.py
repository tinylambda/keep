import io
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

    output_stream = open("yaml_dump_to_file.yaml", "wb")
    io_wrapper = io.TextIOWrapper(output_stream, encoding="utf-8")

    yaml.dump(data, io_wrapper)
    io_wrapper.close()

    input_stream = open("yaml_dump_to_file.yaml", "rb")
    read_wrapper = io.TextIOWrapper(input_stream, encoding="utf-8")
    logging.info("%s", read_wrapper.read())
