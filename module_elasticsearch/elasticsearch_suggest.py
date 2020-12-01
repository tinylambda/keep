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
    index_refresh, index_alias_exists, doc_get, doc_exists, doc_get_source, doc_delete, doc_update, doc_bulk, doc_mget
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'mybooks'


if __name__ == '__main__':
    doc_search(elasticsearch_client, INDEX_NAME, search_body={
        'suggest': {
            'suggest1': {
                'text': 'we find tester',
                'term': {
                    'field': 'description',
                }
            }
        }
    })
