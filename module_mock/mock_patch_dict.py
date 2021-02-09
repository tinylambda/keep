from unittest.mock import patch


if __name__ == '__main__':
    foo = {'key': 'value'}
    original = foo.copy()

    with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
        assert foo == {'newkey': 'newvalue'}

    assert foo == original

