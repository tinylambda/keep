import asyncio
import json
import logging
import typing
import urllib.parse


import aioredis

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class GameConsumer(AsyncWebsocketConsumer):
    PACK_DELIMITER = b'||'

    def __init__(self, *args, **kwargs):
        super(GameConsumer, self).__init__(*args, **kwargs)
        self.server_task_queue_service = None
        self._extra_bytes: bytes = None
        self.logger = logging.getLogger('django')

    @property
    def extra_bytes(self) -> bytes:
        if not self._extra_bytes:
            extra_data = [
                ('channel_name', self.channel_name),
                ('role_id', 1)
            ]
            extra_string = urllib.parse.urlencode(extra_data)
            self._extra_bytes = extra_string.encode('utf-8')
        return self._extra_bytes

    def pack(self, bytes_data: bytes):
        packed_bytes = self.PACK_DELIMITER.join([self.extra_bytes, bytes_data])
        return packed_bytes
    
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('test_groupname', self.channel_name)
        self.server_task_queue_service = await aioredis.create_redis(**settings.SERVER_TASK_QUEUE)

    async def disconnect(self, code):
        await self.cleanup()

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            server_name, _, _ = bytes_data.split(self.PACK_DELIMITER)
            packed_bytes_data = self.pack(bytes_data)
            self.logger.info(f'send data to queue {server_name}')
            await self.server_task_queue_service.lpush(server_name, packed_bytes_data)
        else:
            self.logger.error(f'client send null value to server')

    async def do_send(self, event: typing.Dict):
        content: bytes = event.get('content')
        await self.send(bytes_data=content)

    async def cleanup(self):
        self.server_task_queue_service.close()
        await self.server_task_queue_service.wait_closed()
        await self.close()

