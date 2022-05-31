import asyncio
import copy
import json
import logging
import typing
import urllib.parse


import aioredis

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class GameConsumer(AsyncWebsocketConsumer):
    PACK_DELIMITER = b"||"

    def __init__(self, *args, **kwargs):
        super(GameConsumer, self).__init__(*args, **kwargs)
        self.server_task_queue_service = None
        self._static_header: typing.Dict = None
        self.logger = logging.getLogger("django")

    @property
    def static_header(self) -> typing.Dict:
        if not self._static_header:
            static_header_data = [
                ("channel_name", self.channel_name),
                ("role_id", 1),
            ]
            self._static_header = dict(static_header_data)
        return self._static_header

    def pack(self, header_bytes: bytes, body_bytes: bytes):
        packed_bytes = self.PACK_DELIMITER.join([header_bytes, body_bytes])
        return packed_bytes

    async def connect(self):
        await self.accept()
        self.server_task_queue_service = await aioredis.create_redis(
            **settings.SERVER_TASK_QUEUE
        )

    async def disconnect(self, code):
        await self.cleanup()
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            server_name, action_name, request_body = bytes_data.split(
                self.PACK_DELIMITER
            )

            header: typing.Dict = {}
            header.update(self.static_header)
            header.update(
                {
                    "server_name": server_name.decode(),
                    "action_name": action_name.decode(),
                }
            )
            header_bytes: bytes = urllib.parse.urlencode(header).encode("utf-8")

            packed_bytes_data = self.pack(header_bytes, request_body)
            self.logger.info(f"send data to queue {server_name}")
            await self.server_task_queue_service.lpush(server_name, packed_bytes_data)
        else:
            self.logger.error(f"client send null value to server")

    async def do_send(self, event: typing.Dict):
        content: bytes = event.get("content")
        await self.send(bytes_data=content)

    async def cleanup(self):
        self.server_task_queue_service.close()
        await self.server_task_queue_service.wait_closed()
        await self.close()
