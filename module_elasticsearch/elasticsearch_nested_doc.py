import time

from module_elasticsearch.utils import (
    index_create,
    index_delete,
    index_exists,
    index_put_mapping,
    index_get_mapping,
    doc_index,
    doc_search,
    index_refresh,
)
from module_elasticsearch import elasticsearch_client

INDEX_NAME = "index_for_nested_doc"


if __name__ == "__main__":
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        "properties": {
            "id": {
                "type": "keyword",
            },
            "date": {"type": "date"},
            "customer_id": {"type": "keyword"},
            "sent": {"type": "boolean"},
            "item": {
                "type": "nested",
                "properties": {
                    "name": {"type": "keyword"},
                    "quantity": {"type": "long"},
                    "price": {"type": "double"},
                    "vat": {"type": "double"},
                },
            },
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        "id": 1001,
        "date": "2020-11-11",
        "customer_id": "user_1",
        "sent": False,
        "item": {
            "name": "Huawei Mate 40 Pro 5G",
            "quantity": 55,
            "price": 9999,
            "vat": 67,
        },
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body, refresh=False)
    index_refresh(elasticsearch_client, INDEX_NAME)

    doc_search(elasticsearch_client, INDEX_NAME)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    index_delete(elasticsearch_client, INDEX_NAME)
