import asyncio
import concurrent.futures
import json
import logging
import os.path
import random
import sys
import uuid

import aetcd3
import zmq.asyncio
from aetcd3 import PutEvent, DeleteEvent

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
change the value by commands:
# etcdctl put /test-services/server_x 10.10.1.1

to see what happens
"""


class Service:
    pass


class BattleService(Service):
    SERVICES = {}

    def __init__(self):
        self.service_ready_event = asyncio.Event()
        self.zmq_context = None
        self.socket = None
        self.port_selected = None
        self.service_id = None

    def do_initialization(self):
        self.zmq_context = zmq.asyncio.Context()
        self.socket = self.zmq_context.socket(zmq.REP)
        self.port_selected = self.socket.bind_to_random_port('tcp://*', min_port=49152, max_port=65536, max_tries=64)

    async def synchronize_services(self):
        service_type = self.__class__.__name__
        self.service_id = uuid.uuid4().hex
        service_type_prefix = f'/test-services/{service_type}/'
        register_key = f'/test-services/{service_type}/{self.service_id}'
        logging.info('waiting service to be ready')
        await self.service_ready_event.wait()
        logging.info('service(id=%s) ready!', self.service_id)

        async with aetcd3.client() as client:
            logging.info('register self to register center')
            register_value = json.dumps({
                'ip': 'localhost',
                'port': self.port_selected,
            })
            await client.put(register_key, register_value)

            logging.info('get all services under %s', service_type_prefix)
            async for value, metadata in client.get_prefix(service_type_prefix):
                self.__class__.SERVICES[metadata.key] = json.loads(value)
            logging.info('service(id=%s) get_prefix got <<%s>> services: %s',
                         self.service_id, len(self.__class__.SERVICES), self.__class__.SERVICES.keys())

            logging.info('listening and apply changes under %s', service_type_prefix)
            it, cancel = await client.watch_prefix(service_type_prefix)
            async for event in it:
                logging.info('got event %s', event)
                if isinstance(event, PutEvent):
                    self.__class__.SERVICES[event.key] = json.loads(event.value)
                elif isinstance(event, DeleteEvent):
                    try:
                        del self.__class__.SERVICES[event.key]
                        logging.info('delete %s successfully', self.service_id)
                    except KeyError:
                        logging.info('%s not in services cache', event.key)

                logging.info('service(id=%s) got <%s> services: %s',
                             self.service_id, len(self.__class__.SERVICES), self.__class__.SERVICES.keys())

    async def run(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.synchronize_services())

        self.do_initialization()
        if self.port_selected is not None:
            self.service_ready_event.set()

        while True:
            message = await self.socket.recv()
            logging.info('process message: %s', message)

    @classmethod
    async def start(cls):
        logging.info('[pid=%s] start a new instance of service %s', os.getpid(), cls.__name__)
        instance = cls()
        await instance.run()

    @classmethod
    def start_in_process(cls, n=2):
        running_loop = asyncio.get_event_loop()
        for _ in range(n):
            running_loop.create_task(cls.start())
        running_loop.run_forever()


if __name__ == '__main__':
    # simulate starting services on different servers
    # some node will get all services by using get_prefix call
    process_pool = concurrent.futures.ProcessPoolExecutor()
    results = process_pool.map(BattleService.start_in_process, (2, 2, 2, 2))
