import asyncio

from aioelasticsearch import Elasticsearch


async def go():
    es = Elasticsearch(hosts='127.0.0.1:9200')

    r = await es.search(body={
            'seq_no_primary_term': True,
            'query': {
                'match_all': {}
            }
        })
    print(r)
    await es.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    loop.close()

