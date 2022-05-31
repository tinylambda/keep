import time

from module_elasticsearch.utils import (
    index_create,
    index_delete,
    index_exists,
    index_put_mapping,
    index_get_mapping,
    doc_index,
    doc_search,
    cluster_nodes,
    cluster_health,
    index_put_settings,
    index_get_settings,
    index_shrink,
    index_put_alias,
    index_get_alias,
    index_delete_alias,
)
from module_elasticsearch import elasticsearch_client

INDEX_NAME = "index_for_test"


if __name__ == "__main__":
    indexes = ["a", "b", "c", "d"]
    indexes_str = ",".join(indexes)

    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)
    index_create(elasticsearch_client, INDEX_NAME)

    # for index_name in indexes:
    #     if index_exists(elasticsearch_client, index_name):
    #         index_delete(elasticsearch_client, index_name)
    index_delete(elasticsearch_client, indexes_str + ",x", ignore_unavailable=True)

    for index_name in indexes:
        index_create(elasticsearch_client, index_name)

    # for index_name in indexes:
    #     index_put_alias(elasticsearch_client, index_name, 'good_alias')
    #     index_put_alias(elasticsearch_client, index_name, 'good_alias2')

    index_put_alias(elasticsearch_client, indexes_str, "good_alias")
    index_put_alias(elasticsearch_client, indexes_str, "good_alias2")
    index_get_alias(elasticsearch_client)

    index_delete_alias(elasticsearch_client, "a", "good_alias")
    index_get_alias(elasticsearch_client)

    index_delete(elasticsearch_client, INDEX_NAME)
    index_delete(elasticsearch_client, indexes_str)
    # for index_name in indexes:
    #     index_delete(elasticsearch_client, index_name)
