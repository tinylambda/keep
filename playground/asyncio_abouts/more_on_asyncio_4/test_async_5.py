import asyncio
import os
import signal
import threading
import time

import pytest

from playground.asyncio_abouts.more_on_asyncio_4 import sample_24


@pytest.fixture
def event_loop(event_loop, mocker):
    new_loop = asyncio.get_event_loop_policy().new_event_loop()
    asyncio.set_event_loop(new_loop)
    new_loop._close = new_loop.close
    new_loop.close = mocker.Mock()

    yield new_loop

    getattr(new_loop, "_close")()


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
def mock_queue(mocker, monkeypatch):
    queue = mocker.Mock()
    monkeypatch.setattr(sample_24.asyncio, "Queue", queue)
    return queue.return_value


def test_main(create_mock_coro, event_loop: asyncio.AbstractEventLoop, mock_queue):
    mock_consume, _ = create_mock_coro(
        "playground.asyncio_abouts.more_on_asyncio_4.sample_24.consume"
    )
    mock_publish, _ = create_mock_coro(
        "playground.asyncio_abouts.more_on_asyncio_4.sample_24.publish"
    )
    # mock out 'asyncio.gather' that 'shutdown' calls instead of 'shutdown' itself
    mock_asyncio_gather, _ = create_mock_coro(
        "playground.asyncio_abouts.more_on_asyncio_4.sample_24.asyncio.gather"
    )

    def _send_signal():
        # allow the loop to start and work a little bit...
        time.sleep(0.1)
        # ... then send a signal
        os.kill(os.getpid(), signal.SIGTERM)

    thread = threading.Thread(target=_send_signal, daemon=True)
    thread.start()

    sample_24.main()

    assert signal.SIGTERM in event_loop._signal_handlers
    assert sample_24.handle_exception == event_loop.get_exception_handler()

    mock_asyncio_gather.assert_called_once_with(return_exceptions=True)
    mock_consume.assert_called_once_with(mock_queue)
    mock_publish.assert_called_once_with(mock_queue)

    # asserting the loop is stopped but not closed
    assert not event_loop.is_running()
    assert not event_loop.is_closed()
    event_loop.close.assert_called_once_with()
