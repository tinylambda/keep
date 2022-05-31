import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME, CUSTOMER_INDEX_NAME


if __name__ == "__main__":
    elasticsearch_client.delete_by_query(
        DEFAULT_INDEX_NAME, body={"query": {"match_all": {}}}
    )
