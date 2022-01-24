import logging
import warnings


def validate_option(key, val):
    if key in ('stderr_stream', 'stdout_stream'):
        if not isinstance(val, dict):
            raise ValueError("%r isn't a valid object" % key)
        if 'class' not in val:
            raise ValueError("%r must have a 'class' key" % key)
        if 'refresh_time' in val:
            warnings.warn("'refresh_time' is deprecated and not useful "
                          "anymore for %r" % key)


logging.basicConfig()
logger = logging.getLogger('circus')
