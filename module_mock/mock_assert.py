from unittest.mock import Mock
from unittest.mock import call


if __name__ == "__main__":
    try:
        mock = Mock()
        mock.method()
        mock.method.assert_called()
        mock.method.assert_called_once()
        mock.method()
        mock.method.assert_called_with()
        mock.method(1, 2)
        mock.method.assert_called_with(1, 2)
        mock.method.assert_any_call()  # assert passes if the mock has ever been called

        mock.method.assert_called_with()  # check the most recent call
        mock.method.assert_called_with("foo")
        mock.method.assert_called_once()
    except Exception as e:
        print("1st phrase passed")

    try:
        mock = Mock(return_value=None)
        mock(1)
        mock(2)
        mock(3)
        mock(4)
        calls = [call(2), call(3)]
        mock.assert_has_calls(calls)
        calls = [call(4), call(2), call(3)]
        mock.assert_has_calls(calls, any_order=True)
    except Exception as e:
        print("2nd phrase passed")

    try:
        m = Mock()
        m.hello.assert_not_called()
        obj = m.hello()
        m.hello.assert_not_called()
    except Exception as e:
        print("3rd phrase passed")
