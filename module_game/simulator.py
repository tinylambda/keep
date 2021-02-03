import typing
import asyncio


class Task:
    def __init__(self):
        pass


class User:
    def __init__(self, user_data: typing.Dict):
        self.user_data = user_data
        self.can_sleep = False

    def wakeup(self):
        pass

    def sleep(self):
        pass


class World:
    def __init__(self):
        pass

    def add_user(self, user):
        pass

    def run(self):
        pass


