import asyncio
import json
import logging
import os.path
import socket
import sys
import uuid

import aetcd3
import attr
import zmq.asyncio
from aetcd3 import Event, PutEvent, DeleteEvent

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
change the value by commands:
# etcdctl put /test-services/server_x 10.10.1.1

to see what happens
"""


@attr.s
class BattleService:
    SERVICE_ROOT = '/test-services/'
    SERVICE_LOCK_ROOT = '/test-locks/services/'
    SERVICES = {}

    zmq_context = attr.ib(default=attr.Factory(zmq.asyncio.Context))
    events_buffer = attr.ib(default=attr.Factory(list[Event]))
    service_socket = attr.ib(default=None)
    service_port = attr.ib(default=None)
    service_state = attr.ib(default=None)
    service_register_key = attr.ib(default=None)
    service_register_value = attr.ib(default=None)
    service_stop_event = attr.ib(default=attr.Factory(asyncio.Event))
    found_self_event = attr.ib(default=attr.Factory(asyncio.Event))
    start_core_loop_event = attr.ib(default=attr.Factory(asyncio.Event))
    service_start_listen_service_directory_event = attr.ib(default=attr.Factory(asyncio.Event))
    asyncio_loop = attr.ib(default=attr.Factory(asyncio.get_event_loop))
    service_prepare_semaphore = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.service_socket = self.zmq_context.socket(zmq.REP)
        self.service_port = self.service_socket.bind_to_random_port('tcp://*',
                                                                    min_port=49152,
                                                                    max_port=65535,
                                                                    max_tries=64)
        self.service_state = 'registering'
        unique_id = uuid.uuid4().hex
        self.service_register_key = os.path.join(self.service_directory, unique_id)
        self.service_register_value = json.dumps({
            'host_ip': self.host_ip,
            'port': self.service_port,
        })

    @property
    def service_directory(self):
        return os.path.join(self.__class__.SERVICE_ROOT, self.__class__.__name__)

    @property
    def service_lock(self):
        return os.path.join(self.__class__.SERVICE_LOCK_ROOT, self.__class__.__name__)

    @property
    def host_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception as e:
            logging.debug('Error when try to get local ip address', exc_info=e)
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip

    def get_recv_task(self):
        """receive request data"""
        return self.asyncio_loop.create_task(self.service_socket.recv())

    def new_client_instance(self, host_ip, port):
        instance = self.zmq_context.socket(zmq.REQ)
        instance.connect(f'tcp://{host_ip}:{port}')
        return instance

    def service_cache_add(self, key, value):
        value_dict = json.loads(value)
        instance = self.new_client_instance(**value_dict)
        value_dict.update({'instance': instance})
        self.__class__.SERVICES[key] = value_dict

    def service_cache_del(self, key):
        if key in self.__class__.SERVICES:
            del self.__class__.SERVICES[key]

    def apply_event(self, event: Event):
        key = event.key
        if self.service_state == 'registering':
            if key == self.service_register_key.encode():
                self.found_self_event.set()
            self.events_buffer.append(event)
        else:
            if isinstance(event, PutEvent):
                self.service_cache_add(key, event.value)
            elif isinstance(event, DeleteEvent):
                self.service_cache_del(key)

    def apply_buffered_events(self):
        for event in self.events_buffer:
            self.apply_event(event)

    @staticmethod
    async def get_semaphore(n):
        sem = asyncio.Semaphore(n)
        for _ in range(n):
            await sem.acquire()
        return sem

    @staticmethod
    async def semaphore_trigger(sem: asyncio.Semaphore, event: asyncio.Event, times):
        while times > 0:
            await sem.acquire()
        event.set()

    async def listen_service_directory(self):
        while not self.service_stop_event.is_set():
            try:
                async with aetcd3.client() as client:
                    it, cancel = await client.watch_prefix(self.service_directory)
                    self.service_start_listen_service_directory_event.set()
                    async for event in it:
                        self.apply_event(event)
                        if self.service_stop_event.is_set():
                            break
            except Exception as e:
                logging.info('exception happened will retry', exc_info=e)
        logging.info('stop listening service directory')

    async def fetch_all_service_instances(self):
        async with aetcd3.client() as client:
            async for value, metadata in client.get_prefix(self.service_directory):
                self.service_cache_add(metadata.key, value)

    async def register_self(self):
        async with aetcd3.client() as client:
            await client.put(self.service_register_key, self.service_register_value)

    async def service_say_hi(self):
        logging.info('service [%s] say hi to other service instances', self.service_register_key)
        async with aetcd3.client() as client:
            async with client.lock(self.service_lock):
                self.asyncio_loop.create_task(self.listen_service_directory())
                await self.service_start_listen_service_directory_event.wait()
                logging.info('service_start_listen_service_directory_event set')
                await self.fetch_all_service_instances()
                await self.register_self()

                n_other_services = len(self.__class__.SERVICES)
                self.service_prepare_semaphore = await self.get_semaphore(n_other_services)
                self.start_core_loop_event.set()

                all_confirmed_event = asyncio.Event()
                await self.semaphore_trigger(self.service_prepare_semaphore, all_confirmed_event, n_other_services)
                await all_confirmed_event.wait()

                await self.found_self_event.wait()
                self.service_state = 'registered'
                self.apply_buffered_events()
                logging.info('service_say_hi complete!')

    async def core_loop(self):
        logging.info('core loop: waiting !')
        await self.start_core_loop_event.wait()
        logging.info('core loop: start !')
        # simulate other services confirmation
        while not self.service_stop_event.is_set():
            logging.info('waiting request...')
            await asyncio.sleep(1)
            self.service_prepare_semaphore.release()

    def run(self):
        self.asyncio_loop.create_task(self.core_loop())
        self.asyncio_loop.create_task(self.service_say_hi())
        self.asyncio_loop.run_forever()


if __name__ == '__main__':
    s = BattleService()
    s.run()
