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

INDEX_NAME = 'index_for_percolator'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'q': {
                'type': 'percolator',
            },
            'body': {
                'type': 'text',
            }
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    percolator_doc_body = {
        'q': {
            'match': {
                'body': 'quick brown fox'
            }
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, percolator_doc_body)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME, search_body={
        'query': {
            'percolate': {
                'field': 'q',
                'document': {
                    'body': 'fox'
                }
            }
        }
    })

    index_delete(elasticsearch_client, INDEX_NAME)

