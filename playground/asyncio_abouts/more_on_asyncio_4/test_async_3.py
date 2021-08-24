import pytest
from pytest_mock import mocker
from playground.asyncio_abouts.more_on_asyncio_4 import sample_24


@pytest.fixture
def create_mock_coro(mocker, monkeypatch):
    def _create_mock_patch_coro(to_patch=None):
        mock = mocker.Mock()

        async def _coro(*args, **kwargs):
            return mock(*args, **kwargs)

        if to_patch:
            monkeypatch.setattr(to_patch, _coro)
        return mock, _coro
    return _create_mock_patch_coro


@pytest.fixture
def mock_sleep(create_mock_coro):
    # will not need the returned coroutine here
    mock, _ = create_mock_coro(to_patch='playground.asyncio_abouts.more_on_asyncio_4.sample_24.asyncio.sleep')
    return mock


@pytest.fixture
def message():
    return sample_24.PubSubMessage(message_id='1234', instance_name='mayhem_test')


@pytest.mark.asyncio
async def test_save(mock_sleep, message: sample_24.PubSubMessage):
    assert not message.saved
    await sample_24.save(message)
    assert message.saved
    assert 1 == mock_sleep.call_count
