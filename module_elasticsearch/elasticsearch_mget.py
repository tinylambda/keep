import time

from module_elasticsearch.utils import testing_index
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
    index_rollover,
    index_list,
    index_refresh,
    index_alias_exists,
    doc_get,
    doc_exists,
    doc_get_source,
    doc_delete,
    doc_update,
    doc_bulk,
    doc_mget,
)
from module_elasticsearch import elasticsearch_client
from elasticsearch.helpers import bulk

INDEX_NAME = "index_for_test"


if __name__ == "__main__":
    with testing_index(elasticsearch_client, INDEX_NAME):
        doc_index(elasticsearch_client, INDEX_NAME, {"value1": "1"}, id="1")
        doc_index(elasticsearch_client, INDEX_NAME, {"value1": "2"}, id="2")
        doc_mget(
            elasticsearch_client,
            {
                "docs": [
                    {"_index": INDEX_NAME, "_id": "1"},
                    {"_index": INDEX_NAME, "_id": "2"},
                ]
            },
        )
