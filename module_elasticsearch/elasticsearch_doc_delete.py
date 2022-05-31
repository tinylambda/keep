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
)
from module_elasticsearch import elasticsearch_client

INDEX_NAME = "index_for_test"


if __name__ == "__main__":
    with testing_index(elasticsearch_client, INDEX_NAME):
        doc_id = "xxxxuuu777"
        doc_body = {
            "id": "1234",
            "date": "2020-11-11T12:14:54",
            "customer_id": "customer1",
            "sent": True,
            "in_stock_items": 0,
            "items": [
                {"name": "item1", "quantity": 3, "vat": 20},
                {
                    "name": "item2",
                    "quantity": 2,
                    "vat": 20,
                },
                {
                    "name": "item3",
                    "quantity": 1,
                    "vat": 10,
                },
            ],
        }
        # refresh=True for testing
        doc_index(
            elasticsearch_client, INDEX_NAME, doc_body=doc_body, id=doc_id, refresh=True
        )
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)
        doc_delete(elasticsearch_client, INDEX_NAME, doc_id)
        doc_get(
            elasticsearch_client, INDEX_NAME, doc_id
        )  # here should raise NotFoundError
