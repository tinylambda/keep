import asyncio

from coroutines import f, g, g_ex


async def main():
    result_f, result_g = await asyncio.gather(f(), g_ex(), return_exceptions=True)
    print(result_f, result_g)
    print(isinstance(result_f, BaseException),
          isinstance(result_g, BaseException))

if __name__ == '__main__':
    asyncio.run(main())

'''
Takes many awaitables as *args.
Wraps each awaitable in a task if necessary.
Returns the list of results in the same order.
Allows errors to be returned as results (by passing return_exceptions=True).
Otherwise if one of the awaitables raises an exception, gather() propagates it immediately to the caller. But the remaining tasks keep running.
If gather() itself is canceled, it cancels all unfinished tasks it’s gathering.
'''
