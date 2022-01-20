import sys
import unittest
from unittest import TestSuite, findTestCases
from unittest.mock import patch

from module_unittest.myscript import validate_option


class TestValidateOption(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(True)

    @patch('warnings.warn')
    def test_stdout_stream(self, warn):
        self.assertRaises(
            ValueError, validate_option, 'stdout_stream', 'something')
        self.assertRaises(ValueError, validate_option, 'stdout_stream', {})
        validate_option('stdout_stream', {'class': 'MyClass'})
        validate_option(
            'stdout_stream', {'class': 'MyClass', 'my_option': '1'})
        validate_option(
            'stdout_stream', {'class': 'MyClass', 'refresh_time': 1})
        warn.assert_called_once()

    @patch('warnings.warn')
    def test_stderr_stream(self, warn):
        self.assertRaises(
            ValueError, validate_option, 'stderr_stream', 'something')
        self.assertRaises(ValueError, validate_option, 'stderr_stream', {})
        validate_option('stderr_stream', {'class': 'MyClass'})
        validate_option(
            'stderr_stream', {'class': 'MyClass', 'my_option': '1'})
        validate_option(
            'stderr_stream', {'class': 'MyClass', 'refresh_time': 1})
        warn.assert_called_once()


class EasyTestSuite(TestSuite):
    def __init__(self, name):
        try:
            super(EasyTestSuite, self).__init__(
                findTestCases(sys.modules[name]))
        except KeyError:
            pass


test_suite = EasyTestSuite(__name__)


# python -m nose -vs --with-coverage --cover-package=module_unittest module_unittest/tests
