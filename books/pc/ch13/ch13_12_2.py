import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def func():
    log.critical('a critical error')
    log.debug('a debug message')

# Python 3.9.1 (default, Jan 21 2021, 10:58:50)
# [GCC 10.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from ch13_12_2 import func
# >>> func()
# >>> import logging
# >>> logging.basicConfig()
# >>> func()
# CRITICAL:ch13_12_2:a critical error
# >>>
