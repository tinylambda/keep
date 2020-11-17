from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME, INDEX_FOR_TESTING_TEMPLATE

import datetime


doc = {
    'name': 'Felix',
    'tag': ['Python', 'Go'],
    'item': {
        'name': 'Test',
        'quantity': 100,
    }
}

res = elasticsearch_client.index(index=INDEX_FOR_TESTING_TEMPLATE, body=doc)
elasticsearch_client.indices.forcemerge
print(res)

