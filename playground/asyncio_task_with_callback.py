import asyncio

tasks = []


async def t(name):
    print(f"start task {name}")
    await asyncio.sleep(2)
    print(f"done task {name}")


def task_canceller(t):
    print(f"cancel task {t}")
    t.cancel()
    print(f"cancelled task {t}")


async def main():
    loop = asyncio.get_event_loop()
    for i in range(7):
        name = f"task-{i}"
        task = loop.create_task(t(name))
        tasks.append(task)
        task.cancel()

    for task in tasks:
        task.cancel()

    for task in tasks:
        try:
            await task
        except asyncio.CancelledError:
            print("cancelled....")

    await asyncio.wait(tasks)
    print("All done")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
