import pytest

# If you want to run a block of code after the test with a fixture has run,
# you have to add a finalizer function to the fixture.


@pytest.fixture()
def fixture01(request):
    print('\nIn fixture...')

    def fin():
        print('\nFinalized...')

    request.addfinalizer(fin)


@pytest.mark.usefixtures('fixture01')
def test_case01():
    print('\nI am the test_case01')


# pytest -vs module_pytest/test_fixture_order.py
