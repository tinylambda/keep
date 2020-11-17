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

INDEX_NAME = 'index_for_feature_vector'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'categories': {
                'type': 'rank_features',
            },
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'categories': {
            'sport': 14.2,
            'economic': 24.3
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    doc_body = {
        'categories': {
            'sport': 19.2,
            'economic': 23.1
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME, search_body={
        'query': {
            'rank_feature': {
                'field': 'categories.economic'
            }
        }
    })

    index_delete(elasticsearch_client, INDEX_NAME)

