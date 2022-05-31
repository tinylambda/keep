import asyncio

from aiokafka import AIOKafkaProducer


async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")
    await producer.start()
    try:
        await producer.send_and_wait("my_topic", b"super message")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(send_one())
