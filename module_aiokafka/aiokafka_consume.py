import asyncio

from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        bootstrap_servers='localhost:9092',
        group_id='my-group'
    )
    await consumer.start()
    i = 0
    try:
        async for msg in consumer:
            print('consumed: ', msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
            i += 1
            if i % 100 == 0:
                print(i)
    finally:
        print('Finally: ', i)
        await consumer.stop()


if __name__ == '__main__':
    asyncio.run(consume())


