import asyncio
import aiozmq.rpc


class ServerHandler(aiozmq.rpc.AttrHandler):
    @aiozmq.rpc.method
    def remote_func(self, a: int, b: int) -> int:
        return a + b

    @aiozmq.rpc.method
    def test_func(self, x):
        return x * 4


async def go():
    server = await aiozmq.rpc.serve_rpc(ServerHandler(), bind='tcp://127.0.0.1:5555')
    client = await aiozmq.rpc.connect_rpc(connect='tcp://127.0.0.1:5555')

    ret = await client.call.remote_func(1, 2)
    print('result: ', ret)
    assert 3 == ret

    ret = await client.call.test_func(100)
    print(ret)

    server.close()
    client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())

