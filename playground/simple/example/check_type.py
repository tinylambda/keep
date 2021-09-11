import asyncio
import inspect
import types


async def coroutine():
    pass


def normal():
    pass


if __name__ == '__main__':
    print(inspect.iscoroutinefunction(coroutine))  # 判断是否是协程函数
    print(inspect.iscoroutinefunction(normal))

    coro = coroutine()
    print(isinstance(coro, types.CoroutineType))  # 判断是否是协程

    asyncio.run(coro)
