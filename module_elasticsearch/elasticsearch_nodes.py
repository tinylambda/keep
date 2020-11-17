import time

from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search, cluster_nodes, cluster_health, index_put_settings, index_get_settings, index_shrink
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)
    index_create(elasticsearch_client, INDEX_NAME, body={
        'settings': {
            'index.number_of_shards': 2
        }
    })

    REDUCED_INDEX = 'reduced_index'
    if index_exists(elasticsearch_client, REDUCED_INDEX):
        index_delete(elasticsearch_client, REDUCED_INDEX)

    index_get_settings(elasticsearch_client, INDEX_NAME)
    cluster_nodes(elasticsearch_client)
    cluster_health(elasticsearch_client)

    index_put_settings(elasticsearch_client, INDEX_NAME, setting_body={
        'settings': {
            'index.routing.allocation.require._name': 'cdhilmrstw',
            'index.blocks.write': False,
        }
    })
    doc_index(elasticsearch_client, INDEX_NAME, doc_body={
        'hello': 'world'
    })
    index_get_settings(elasticsearch_client, INDEX_NAME)
    cluster_health(elasticsearch_client)

    index_put_settings(elasticsearch_client, INDEX_NAME, setting_body={
        'index.blocks.write': True,
    })
    index_get_settings(elasticsearch_client, INDEX_NAME)

    index_put_settings(elasticsearch_client, INDEX_NAME, setting_body={
        'index': {
            'number_of_replicas': 7,
            'refresh_interval': '-1',
            'blocks.write': False,
        }
    })
    index_get_settings(elasticsearch_client, INDEX_NAME)

    # index_shrink(elasticsearch_client, INDEX_NAME, REDUCED_INDEX, body={
    #     'settings': {
    #         'index.number_of_replicas': 1,
    #         'index.number_of_shards': 1,
    #         'index.codec': 'best_compression',
    #     },
    #     'aliases': {
    #         'my_search_indices': {}
    #     }
    # })
    # index_get_settings(elasticsearch_client, REDUCED_INDEX)

    index_delete(elasticsearch_client, INDEX_NAME)

