import time

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
    index_refresh, index_alias_exists
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    for index_name in index_get_alias(elasticsearch_client, 'logs_write', ignore_unavailable=True):
        index_delete(elasticsearch_client, index_name)

    if index_exists(elasticsearch_client, 'mylogs-000001'):
        index_delete(elasticsearch_client, 'mylogs-000001')

    index_create(elasticsearch_client, 'mylogs-000001', body={
        'aliases': {
            'logs_write': {'is_write_index': True}
        }
    })

    index_rollover(elasticsearch_client, 'logs_write', body={
        'conditions': {
            'max_age': '7d',
            'max_docs': 10,
            'max_size': '5gb'
        },
        'settings': {
            'index.number_of_shards': 7
        }
    })

    # now index 11 docs
    for i in range(11):
        doc_body = {'type': 'test', 'num': i}
        doc_index(elasticsearch_client, 'logs_write', doc_body)
    index_refresh(elasticsearch_client, 'logs_write')

    index_list(elasticsearch_client)
    doc_search(elasticsearch_client, 'logs_write')

    index_rollover(elasticsearch_client, 'logs_write', body={
        'conditions': {
            'max_age': '7d',
            'max_docs': 7,
            'max_size': '5gb'
        },
        'settings': {
            'index.number_of_shards': 7
        }
    })
    #
    # # now index 11 docs
    # for i in range(11):
    #     doc_body = {'type': 'test', 'num': i}
    #     doc_index(elasticsearch_client, 'logs_write', doc_body)
    # index_refresh(elasticsearch_client, 'logs_write')
    #
    index_list(elasticsearch_client)
    doc_search(elasticsearch_client, 'logs_write')
    #
    #
    #
    #
    #
