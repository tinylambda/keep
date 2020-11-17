import time

from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_field_alias'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)

    mapping_body = {
        'properties': {
            'id': {'type': 'keyword'},
            'date': {'type': 'date'},
            'customer_id': {'type': 'keyword'},
            'sent': {'type': 'boolean'},
            'item': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'keyword'},
                    'quantity': {'type': 'long'},
                    'cost': {
                        'type': 'alias',
                        'path': 'item.price',
                    },
                    'price': {'type': 'double'},
                    'vat': {'type': 'double'},
                }
            }
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'id': '1',
        'date': '2020-11-12T20:07:45Z',
        'customer_id': '100',
        'sent': True,
        'item': [
            {
                'name': 'tshirt',
                'quantity': 10,
                'price': 4.3,
                'vat': 8.5,
            }, {
                'name': 'Huawei Mate 40 Pro',
                'quantity': 2,
                'price': '8888',
                'vat': '7.7',
            }
        ]
    }

    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    search_body = {
        'query': {
            'term': {
                'item.cost': 4.3
            }
        }
    }
    doc_search(elasticsearch_client, INDEX_NAME, search_body=search_body)
    index_delete(elasticsearch_client, INDEX_NAME)



