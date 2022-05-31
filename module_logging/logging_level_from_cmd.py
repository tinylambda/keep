import sys
import logging


loglevel = sys.argv[1]

numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: %s" % loglevel)

logging.basicConfig(level=numeric_level)
