import time

from module_elasticsearch.utils import (
    index_create,
    index_delete,
    index_exists,
    index_put_mapping,
    index_get_mapping,
    doc_index,
    doc_search,
)
from module_elasticsearch import elasticsearch_client

INDEX_NAME = "index_for_test"


if __name__ == "__main__":
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "standard",
                "search_analyzer": "simple",
            },
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    index_delete(elasticsearch_client, INDEX_NAME)
