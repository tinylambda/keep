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
    cluster_info
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)

    settings_body = {
        'index': {
            'number_of_replicas': 2,
            'refresh_interval': '-1',
        },
    }
    index_put_settings(elasticsearch_client, INDEX_NAME, settings_body)
    index_get_settings(elasticsearch_client, INDEX_NAME)

    cluster_info(elasticsearch_client)
    index_delete(elasticsearch_client, INDEX_NAME)

