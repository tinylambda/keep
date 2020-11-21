import time

from module_elasticsearch.utils import testing_index
from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search, cluster_nodes, cluster_health, \
    index_put_settings, index_get_settings, \
    index_shrink, index_put_alias, index_get_alias,\
    index_delete_alias, index_rollover, index_list, \
    index_refresh, index_alias_exists, doc_get, doc_exists, doc_get_source, doc_delete, doc_update, doc_bulk
from module_elasticsearch import elasticsearch_client
from elasticsearch.helpers import bulk

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    with testing_index(elasticsearch_client, INDEX_NAME):
        bulk_body = [
            {'index': {'_index': INDEX_NAME, '_id': '1'}},
            {'field1': 'value1'},
            {'delete': {'_index': INDEX_NAME, '_id': '2'}},
            {'create': {'_index': INDEX_NAME, '_id': '3'}},
            {'field1': 'value3'},
            {'update': {'_index': INDEX_NAME, '_id': '1'}},
            {'doc': {'field2': 'value2'}},
        ]
        doc_bulk(elasticsearch_client, bulk_body, refresh=True)
        doc_search(elasticsearch_client, INDEX_NAME)
