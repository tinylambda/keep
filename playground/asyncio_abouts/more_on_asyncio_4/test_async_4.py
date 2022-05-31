import asyncio

import pytest

from playground.asyncio_abouts.more_on_asyncio_4 import sample_24


@pytest.fixture
def mock_queue(mocker, monkeypatch):
    queue = mocker.Mock()
    monkeypatch.setattr(sample_24.asyncio, "Queue", queue)
    return queue.return_value


@pytest.fixture
def mock_get(mock_queue, create_mock_coro):
    mock_get, coro_get = create_mock_coro()
    mock_queue.get = coro_get
    return mock_get


@pytest.fixture
def message():
    return sample_24.PubSubMessage(message_id="1234", instance_name="mayhem_test")


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


@pytest.mark.asyncio
async def test_consume(mock_get, mock_queue, message, create_mock_coro):
    mock_get.side_effect = [message, Exception("break while loop")]
    mock_handle_message, _ = create_mock_coro(
        "playground.asyncio_abouts.more_on_asyncio_4.sample_24.handle_message"
    )

    with pytest.raises(Exception, match="break while loop"):
        await sample_24.consume(mock_queue)

    ret_tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    assert 1 == len(ret_tasks)
    mock_handle_message.assert_not_called()

    await asyncio.gather(*ret_tasks)
    mock_handle_message.assert_called_once_with(message)
