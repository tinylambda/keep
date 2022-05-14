import pytest


@pytest.fixture()
def fixture01():
    print('\nIn fixture01()...')


@pytest.mark.usefixtures('fixture01')
class TestClass03:
    def test_case01(self):
        print('I am the test_case01')

    def test_case02(self):
        print('I am the test_case02')


# pytest -vs module_pytest/test_fixture_class.py
