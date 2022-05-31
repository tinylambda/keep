import asyncio
import json

import websockets


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    uri = "wss://ws-feed.pro.coinbase.com"

    sub_msg = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-EUR",
                ],
            }
        ],
    }
    sub_msg = json.dumps(sub_msg)
    sub_msg_bytes = sub_msg.encode("utf-8")

    async def reader():
        async with websockets.connect(uri) as ws:
            await ws.send(sub_msg_bytes)

            while True:
                # task for recv from ws
                msg = await ws.recv()
                print(msg)

    loop.run_until_complete(reader())
