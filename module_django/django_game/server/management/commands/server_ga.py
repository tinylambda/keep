import asyncio
import logging

from django.core.management.base import BaseCommand, CommandError

from server.servers.server_ga import ServerGa

logging.getLogger().setLevel(logging.DEBUG)


class Command(BaseCommand):
    help = "Start game server"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.server = None
        self.loop = asyncio.get_event_loop()

    def add_arguments(self, parser):
        pass

    async def start_server(self):
        self.server = ServerGa()
        await self.server.start()

    async def stop_server(self):
        await self.server.stop()

    def handle(self, *args, **options):
        try:
            self.loop.run_until_complete(self.start_server())
        except KeyboardInterrupt:
            self.loop.run_until_complete(self.stop_server())
            self.loop.close()
        self.stdout.write(self.style.SUCCESS("Done"))
