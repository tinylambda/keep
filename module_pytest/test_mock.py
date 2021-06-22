from unittest import mock

import pytest
import requests


class WhereIsPythonError(Exception):
    pass


def is_python_still_a_programming_language():
    try:
        r = requests.get('http://python.org')
    except IOError:
        pass
    else:
        if r.status_code == 200:
            return b'Python is a programming language' in r.content
    raise WhereIsPythonError('something bad happened')


def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content

    def fake_get(url):
        return m

    return fake_get


def raise_get(url):
    raise IOError('Unable to fetch url %s' % url)


@mock.patch('requests.get', get_fake_get(200, b'Python is a programming language for sure'))
def test_python_is():
    assert is_python_still_a_programming_language() is True


@mock.patch('requests.get', get_fake_get(200, b'Python is no more a programming language'))
def test_python_is_not():
    assert is_python_still_a_programming_language() is False


@mock.patch('requests.get', get_fake_get(404, 'Whatever'))
def test_bad_status_code():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()


@mock.patch('requests.get', raise_get)
def test_ioerror():
    with pytest.raises(WhereIsPythonError):
        is_python_still_a_programming_language()

