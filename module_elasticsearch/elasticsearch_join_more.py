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
)
from module_elasticsearch import elasticsearch_client

INDEX_NAME = "index_for_test"


if __name__ == "__main__":
    with testing_index(elasticsearch_client, INDEX_NAME):
        index_put_mapping(
            elasticsearch_client,
            INDEX_NAME,
            {
                "properties": {
                    "my_id": {
                        "type": "keyword",
                    },
                    "my_join_field": {
                        "type": "join",
                        "relations": {
                            "question": "answer",
                        },
                    },
                }
            },
        )

        index_get_mapping(elasticsearch_client, INDEX_NAME)

        # index questions
        doc_index(
            elasticsearch_client,
            INDEX_NAME,
            {
                "my_id": "1",
                "text": "This is a question",
                "my_join_field": {"name": "question"},
            },
            id="1",
        )

        doc_index(
            elasticsearch_client,
            INDEX_NAME,
            {
                "my_id": "2",
                "text": "This is another question",
                "my_join_field": {
                    "name": "question",
                },
            },
            id="2",
        )

        # index answers to question '1'
        # The routing value is mandatory because parent and child documents must be indexed on the same shard
        doc_index(
            elasticsearch_client,
            INDEX_NAME,
            {
                "my_id": "3",
                "text": "This is an answer",
                "my_join_field": {"name": "answer", "parent": "1"},
            },
            routing="1",
            id="3",
        )

        doc_index(
            elasticsearch_client,
            INDEX_NAME,
            {
                "my_id": "4",
                "text": "This is another answer",
                "my_join_field": {"name": "answer", "parent": "1"},
            },
            routing="1",
            id="4",
        )

        doc_index(
            elasticsearch_client,
            INDEX_NAME,
            {
                "my_id": "5",
                "text": "answer for question 2",
                "my_join_field": {
                    "name": "answer",
                    "parent": "2",
                },
            },
            routing="1",
            id="5",
        )

        index_refresh(elasticsearch_client, INDEX_NAME)

        doc_search(
            elasticsearch_client,
            INDEX_NAME,
            search_body={
                "query": {"parent_id": {"type": "answer", "id": "2"}},
                "aggs": {
                    "parents": {
                        "terms": {
                            "field": "my_join_field#question",
                            "size": 10,
                        }
                    }
                },
                "script_fields": {
                    "parent": {
                        "script": {
                            "source": 'doc["my_join_field#question"]',
                        }
                    }
                },
            },
        )
