import asyncio

from aioelasticsearch import Elasticsearch


async def go(client):
    # r = await client.search(body={
    #         'seq_no_primary_term': True,
    #         'query': {
    #             'match_all': {}
    #         }
    #     })
    sample_data = {'go': 'up'}
    r = await client.index(index='default', body=sample_data)
    print(r)


async def main(n):
    es = Elasticsearch(hosts='127.0.0.1:9200')
    eloop = asyncio.get_event_loop()
    try:
        tasks = [
           eloop.create_task(go(client=es)) for _ in range(n)
        ]
        await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    finally:
        await es.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(1000))
    loop.close()

