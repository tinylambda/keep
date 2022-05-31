import pytest


@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print("Fixture scope:", str(request.scope))
    print("Function Name:", str(request.function.__name__))
    print("Class Name:", str(request.cls))
    print("Module Name:", str(request.module.__name__))
    print("File Path:", str(request.fspath))


@pytest.mark.usefixtures("fixture01")
def test_case01():
    print("I am the test_case01")


# pytest -vs module_pytest/test_fixture_info_access.py
# Output:================================================ test session starts ========================================
# cachedir: .pytest_cache
# rootdir: /Users/Felix/PycharmProjects/keep
# plugins: anyio-3.3.1, asyncio-0.15.1, mock-3.6.1
# collected 1 item
#
# module_pytest/test_fixture_info_access.py::test_case01
# In fixture...
# Fixture scope: function
# Function Name: test_case01
# Class Name: None
# Module Name: module_pytest.test_fixture_info_access
# File Path: /Users/Felix/PycharmProjects/keep/module_pytest/test_fixture_info_access.py
# I am the test_case01
# PASSED
