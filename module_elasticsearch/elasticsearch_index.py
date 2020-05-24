from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME

import datetime


doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.datetime.now()
}

res = elasticsearch_client.index(index=DEFAULT_INDEX_NAME, body=doc)
print(res)

