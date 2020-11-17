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
    index_open, \
    index_close
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    index_close(elasticsearch_client, INDEX_NAME)
    try:
        doc_search(elasticsearch_client, INDEX_NAME)  # should raise exception here
    finally:
        index_delete(elasticsearch_client, INDEX_NAME)

