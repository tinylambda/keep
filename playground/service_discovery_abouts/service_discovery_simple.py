import asyncio
import json
import logging
import os.path
import random
import sys
import uuid

import aetcd3
from aetcd3 import PutEvent, DeleteEvent

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
change the value by commands:
# etcdctl put /test-services/server_x 10.10.1.1

to see what happens
"""

SERVICE_REGISTRY_PREFIX = "/test-services/"
SERVICE_TYPES = ["battle", "role", "account", "assemble", "npc"]


async def register_service(key, value):
    async with aetcd3.client() as client:
        await client.put(key, value)


async def start_service(service_type, i):
    preparing_seconds = random.randint(0, 3)
    await asyncio.sleep(preparing_seconds)
    port = random.randint(8000, 65535)

    service_id = uuid.uuid4().hex
    register_key = os.path.join(SERVICE_REGISTRY_PREFIX, service_type, service_id)
    register_value = json.dumps(
        {
            "ip": "localhost",
            "port": port,
        }
    )

    logging.info(
        "service [] started: %s, listening on port: %s, "
        "is ready to serve requests, now register self to etcd [%s]",
        i,
        port,
        register_key,
    )
    await register_service(register_key, register_value)


async def service_creator(n=10):
    """simulate service start process"""
    for i in range(n):
        service_type = random.choice(SERVICE_TYPES)
        await start_service(service_type, i)


async def service_caller(service_type):
    current_services = {}

    async with aetcd3.client() as client:
        service_prefix = os.path.join(SERVICE_REGISTRY_PREFIX, service_type)

        logging.info("initialize current_services of type %s", service_type)
        async for value, metadata in client.get_prefix(service_prefix):
            instance_config = json.loads(value)
            current_services[metadata.key] = instance_config

        logging.info("watch service change of type %s", service_type)
        it, cancel = await client.watch_prefix(service_prefix)
        async for event in it:
            if isinstance(event, PutEvent):
                current_services.update({event.key: json.loads(event.value)})
            elif isinstance(event, DeleteEvent):
                del current_services[event.key]

            logging.info(
                "current services of type %s is %s", service_type, current_services
            )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(service_creator(100))
    loop.create_task(service_caller("battle"))
    loop.create_task(service_caller("role"))
    loop.create_task(service_caller("npc"))
    loop.create_task(service_caller("account"))
    loop.create_task(service_caller("assemble"))
    loop.run_forever()
