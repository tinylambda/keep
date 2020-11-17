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
    index_close, index_flush, index_forcemerge
from module_elasticsearch import elasticsearch_client


INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'hello': 'world'
    }

    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    index_flush(elasticsearch_client, INDEX_NAME)
    index_forcemerge(elasticsearch_client, INDEX_NAME)

    index_delete(elasticsearch_client, INDEX_NAME)


