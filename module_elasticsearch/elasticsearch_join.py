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

INDEX_NAME = 'index_for_join_docs'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'join_field': {
                'type': 'join',
                'relations': {
                    'order': 'item'
                }
            },
            'id': {'type': 'keyword'},
            'date': {'type': 'date'},
            'customer_id': {'type': 'keyword'},
            'sent': {'type': 'boolean'},
            'name': {'type': 'text'},
            'quantity': {'type': 'integer'},
            'vat': {'type': 'double'},
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    # index parent
    parent_doc = {
        'id': '1',
        'date': '2020-11-11T20:07:45Z',
        'customer_id': '100',
        'sent': True,
        'join_field': 'order',
    }
    doc_index(elasticsearch_client, INDEX_NAME, parent_doc, id=1)

    # index child
    child_doc = {
        'id': 'c1',
        'name': 'tshirt',
        'quantity': 10,
        'price': 4.3,
        'vat': 8.5,
        'join_field': {
            'name': 'item',
            'parent': '1'
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, child_doc, id='c1', routing=1)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME)

    index_delete(elasticsearch_client, INDEX_NAME)

