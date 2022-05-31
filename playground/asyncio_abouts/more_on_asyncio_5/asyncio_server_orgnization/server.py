import asyncio
import concurrent.futures
import logging
import random
import string
import sys
import threading

from uhashring import HashRing

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class ServerMeta(type):
    BASE_SERVER_NAME = "Server"

    def __new__(mcs, clsname, bases, class_dict: dict):
        server_type = class_dict.get("SERVER_TYPE")
        if not clsname == mcs.BASE_SERVER_NAME:
            if server_type is None:
                raise AttributeError("a server must specify SERVER_TYPE at class level")

        if "SERVICES" not in class_dict:
            class_dict["SERVICES"] = list()

        if "HASH_RING" not in class_dict:
            class_dict["HASH_RING"] = HashRing(nodes=[])

        cls = type.__new__(mcs, clsname, bases, class_dict)
        return cls

    def __init__(cls, *args, **kwargs):
        print("meta init", args, kwargs)
        super().__init__(*args, **kwargs)


class Server(metaclass=ServerMeta):
    SERVER_TYPE = None

    def __init__(self):
        print("Server init")

    @classmethod
    def install_loop(cls):
        if threading.current_thread() is not threading.main_thread():
            logging.info("installing loop in non-main thread")
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)

    @classmethod
    async def listen(cls):
        # here we simulate watching etcd key to get updated server info
        while True:
            logging.info("waiting etcd to update")
            random_i = random.randint(1, 20)
            await asyncio.sleep(random.randint(1, 20))  # simulate wait time
            services = [
                "".join(random.choices(string.ascii_lowercase, k=2))
                for _ in range(random_i)
            ]
            cls.SERVICES.clear()
            cls.SERVICES.extend(services)
            cls.HASH_RING = HashRing(nodes=cls.SERVICES)

    @classmethod
    async def print_services(cls):
        while True:
            logging.info(
                "current services: %s, user001 goto service: %s",
                cls.SERVICES,
                cls.HASH_RING.get_node("user001"),
            )
            await asyncio.sleep(4)

    @classmethod
    def start(cls):
        instance = cls()
        instance.install_loop()
        loop = asyncio.get_event_loop()
        loop.create_task(cls.listen())
        loop.create_task(cls.print_services())
        print("start server")
        loop.run_forever()


class ServerBattle(Server):
    SERVER_TYPE = "battle"

    def __init__(self):
        super().__init__()
        self.good = "good"
        print("ServerBattle init")


class ServerAssembly(Server):
    SERVER_TYPE = "assembly"


async def coroutine_worker():
    while True:
        await asyncio.sleep(1)
        print(
            "threading: ",
            threading.current_thread().getName(),
            " loop id: ",
            id(asyncio.get_event_loop()),
        )


def do_test(name):
    if threading.current_thread() is not threading.main_thread():
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)

    event_loop = asyncio.get_event_loop()
    print("the loop id is: ", id(event_loop), name)
    event_loop.run_until_complete(coroutine_worker())
    return 100


def simple_test(item):
    return 100


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # thread_executor = concurrent.futures.ThreadPoolExecutor()
    # process_executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    #
    # results = process_executor.map(do_test, ['a', 'b'])
    # for item in results:
    #     print(item)

    # ServerBattle()
    ServerBattle.start()
