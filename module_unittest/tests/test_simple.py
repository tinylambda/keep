import random
import unittest


class TestValidateOption(unittest.TestCase):
    port = random.randint(20000, 30000)

    def setUp(self) -> None:
        self.rand = random.random()
        print("in self setup")

    def tearDown(self) -> None:
        print("in self tearDown")

    def test_simple(self):
        print("do simple test", self.rand, self.port)
        self.assertTrue(True)

    def test_simple2(self):
        print("do simple test 2", self.rand, self.port)
        self.assertTrue(True)


# python -m nose -vs --with-coverage --cover-package=module_unittest module_unittest/tests
