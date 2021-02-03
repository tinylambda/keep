import asyncio
import binascii
import os

from aiokafka import AIOKafkaProducer


async def send(producer, topic: str):
    sender_id = binascii.hexlify(os.urandom(16))
    print(f'Sender<{sender_id}> Start')

    for i in range(100):
        msg_in_bytes = sender_id + b'|||||' + str(i).encode()
        await producer.send_and_wait(topic, msg_in_bytes)

    print(f'Sender<{sender_id}> Done')


async def send_concurrently():
    loop = asyncio.get_event_loop()
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    topic = 'my_topic'
    await producer.start()

    try:
        tasks = [
            loop.create_task(send(producer, topic))
            for _ in range(100)
        ]
        await asyncio.wait(tasks)
        print('All Done')
        # await producer.send_and_wait('my_topic', b'super message')
    finally:
        await producer.stop()


if __name__ == '__main__':
    asyncio.run(send_concurrently())


