import logging
import logging.handlers
import os
import unittest
from syslog import LOG_USER

from papa import Papa

from module_unittest.myscript import logger

LOG_FMT = r"%(asctime)s %(name)s[%(process)d] [%(levelname)s] %(message)s"


class TestMaybeBlock(unittest.TestCase):
    def setUp(self):
        self.saved = os.environ.copy()

    def tearDown(self):
        os.environ = self.saved

    def test_one(self):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        datefmt = r"%b %d %H:%M:%S"
        handler = logging.handlers.SysLogHandler(
            address=("localhost", 514), facility=LOG_USER
        )
        formatter = logging.Formatter(fmt=LOG_FMT, datefmt=datefmt)
        handler.setFormatter(formatter)
        root_logger.handlers = [handler]

    def test_two(self):
        with Papa() as p:
            logger.info("got two")

    def test_three(self):
        with Papa() as p:
            logger.info("got three")
