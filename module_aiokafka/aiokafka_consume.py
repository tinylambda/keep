import asyncio

from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        bootstrap_servers='localhost:9092',
        group_id='my-group'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print('consumed: ', msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()


if __name__ == '__main__':
    asyncio.run(consume())


