import asyncio
import pytest

from playground.asyncio_abouts.more_on_asyncio_4 import sample_24


@pytest.fixture
def message():
    return sample_24.PubSubMessage(message_id="1234", instance_name="mayhem_test")


def test_save(message: sample_24.PubSubMessage):
    assert not message.saved
    asyncio.run(sample_24.save(message))
    assert message.saved


def test_save_2(message: sample_24.PubSubMessage):
    assert not message.saved
    loop = (
        asyncio.new_event_loop()
    )  # note : we should use new_event_loop() instead of get_event_loop()
    loop.run_until_complete(sample_24.save(message))
    loop.close()
    assert message.saved


def test_save_3(message: sample_24.PubSubMessage):
    assert not message.saved
    loop = asyncio.new_event_loop()
    loop.run_until_complete(sample_24.save(message))
    loop.close()
    assert message.saved


#  pytest -v playground/asyncio_abouts/more_on_asyncio_4
