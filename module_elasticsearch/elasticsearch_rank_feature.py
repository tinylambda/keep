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
            'pr': {
                'type': 'rank_feature',
            },
            'url_length': {
                'type': 'rank_feature',
                'positive_score_impact': False,
            }
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'pr': 5,
        'url_length': 20
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    doc_body = {
        'pr': 2,
        'url_length': 11,
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME, search_body={
        'query': {
            'rank_feature': {
                'field': 'url_length'
            }
        }
    })

    index_delete(elasticsearch_client, INDEX_NAME)

