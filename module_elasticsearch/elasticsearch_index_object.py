from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME

import datetime


doc = {
    'name': 'Felix',
    'tag': ['Python', 'Go'],
    'email': 'tinylambda@gmail.com',
    'item': {
        'name': 'The Python Programming Language',
        'quantity': 10
    }
}

res = elasticsearch_client.index(index=DEFAULT_INDEX_NAME, body=doc)
print(res)

