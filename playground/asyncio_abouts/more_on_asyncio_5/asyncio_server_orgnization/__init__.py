import asyncio
import concurrent.futures
import threading
import time


class ServerMeta(type):
    BASE_SERVER_NAME = 'Server'

    def __new__(mcs, clsname, bases, class_dict: dict):
        server_type = class_dict.get('SERVER_TYPE')
        if not clsname == mcs.BASE_SERVER_NAME:
            if server_type is None:
                raise AttributeError('a server must specify SERVER_TYPE at class level')

        if 'SERVICES' not in class_dict:
            class_dict['SERVICES'] = list()

        cls = type.__new__(mcs, clsname, bases, class_dict)
        return cls

    def __init__(cls, *args, **kwargs):
        # print('meta init')
        super().__init__(*args, **kwargs)


class Server(metaclass=ServerMeta):
    SERVER_TYPE = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        print('Server init')

    @classmethod
    def start(cls):
        instance = cls()
        print('start server', cls, instance, dir(instance))


class ServerBattle(Server):
    SERVER_TYPE = 'battle'

    def __init__(self):
        super().__init__()
        self.good = 'good'
        print('ServerBattle init')


class ServerAssembly(Server):
    SERVER_TYPE = 'assembly'


async def coroutine_worker():
    while True:
        await asyncio.sleep(1)
        print('threading: ', threading.current_thread().getName(), ' loop id: ', id(asyncio.get_event_loop()))


def do_test(name):
    if threading.current_thread() is not threading.main_thread():
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)

    event_loop = asyncio.get_event_loop()
    print('the loop id is: ', id(event_loop), name)
    event_loop.run_until_complete(coroutine_worker())
    return 100


def simple_test(item):
    return 100


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    thread_executor = concurrent.futures.ThreadPoolExecutor()
    process_executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)

    results = process_executor.map(do_test, ['a', 'b'])
    for item in results:
        print(item)
