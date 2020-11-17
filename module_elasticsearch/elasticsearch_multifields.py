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

INDEX_NAME = 'index_for_multifields'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'name': {
                'type': 'keyword',
                'fields': {
                    'name': {'type': 'keyword'},
                    'tk': {'type': 'text'},
                    # 'code': {'type': 'text', 'analyzer': 'code_analyzer'},
                }
            }
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'name': 'Huawei Mate 40 Pro 5G',
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    search_body = {
        '_source': ['name', ],
        'query': {
            'match_all': {}
        }
    }
    doc_search(elasticsearch_client, INDEX_NAME, search_body=search_body)

