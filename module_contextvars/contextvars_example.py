import asyncio
import contextvars


current_request_id_ctx = contextvars.ContextVar('current_request_id_ctx')
current_request_id_global = ''


async def some_inner_coroutine():
    global current_request_id_global

    # simulate some async work
    await asyncio.sleep(0.1)

    # get value
    print(f'Processed inner coroutine of request: {current_request_id_ctx.get()}')
    if current_request_id_global != current_request_id_ctx.get():
        print(f'ERROR! global var={current_request_id_global}')


async def some_outer_coroutine(req_id):
    global current_request_id_global

    # set value
    current_request_id_ctx.set(req_id)
    current_request_id_global = req_id

    await some_inner_coroutine()

    # get value
    print(f'Processed outer coroutine of request: {current_request_id_ctx.get()}\n')


async def main():
    tasks = []
    for req_id in range(1, 10000):
        tasks.append(asyncio.create_task(some_outer_coroutine(req_id)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
