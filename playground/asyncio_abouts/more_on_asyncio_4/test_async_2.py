import pytest

from playground.asyncio_abouts.more_on_asyncio_4 import sample_24


@pytest.fixture
def message():
    return sample_24.PubSubMessage(message_id='1234', instance_name='mayhem_test')


@pytest.mark.asyncio
async def test_save(message: sample_24.PubSubMessage):
    assert not message.saved
    await sample_24.save(message)
    assert message.saved

# depends on pytest-asyncio module
#  pytest -v playground/asyncio_abouts/more_on_asyncio_4
