import time

from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search, \
    index_get_settings, \
    index_put_settings, \
    cluster_health, \
    index_reindex
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'
INDEX_NAME_COPY = 'index_for_test_copy'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    if index_exists(elasticsearch_client, INDEX_NAME_COPY):
        index_delete(elasticsearch_client, INDEX_NAME_COPY)

    index_create(elasticsearch_client, INDEX_NAME)
    index_create(elasticsearch_client, INDEX_NAME_COPY)

    setting_body = {
        'number_of_replicas': 1,
    }
    mapping_body = {
        'properties': {
            'id': {'type': 'keyword'}
        }
    }
    index_put_settings(elasticsearch_client, INDEX_NAME, setting_body)
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)

    doc_body = {
        'id': '1000'
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)

    # Now we want to change some mapping
    setting_body_new = {
        'number_of_replicas': 2,
    }
    mapping_body_new = {
        'properties': {
            'id': {'type': 'long'}
        }
    }
    # index_put_settings(elasticsearch_client, INDEX_NAME, setting_body_new)  # works
    # index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body_new)  # won't work
    index_put_settings(elasticsearch_client, INDEX_NAME_COPY, setting_body_new)
    index_put_mapping(elasticsearch_client, INDEX_NAME_COPY, mapping_body_new)

    # reindex using the new mapping
    index_reindex(elasticsearch_client, reindex_body={
        'source': {
            'index': INDEX_NAME
        },
        'dest': {
            'index': INDEX_NAME_COPY
        }
    })

    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME)
    doc_search(elasticsearch_client, INDEX_NAME_COPY)

    index_get_settings(elasticsearch_client, INDEX_NAME)
    index_get_settings(elasticsearch_client, INDEX_NAME_COPY)

    index_delete(elasticsearch_client, INDEX_NAME)
    index_delete(elasticsearch_client, INDEX_NAME_COPY)

