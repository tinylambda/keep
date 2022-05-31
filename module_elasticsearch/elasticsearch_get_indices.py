import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME, CUSTOMER_INDEX_NAME


if __name__ == "__main__":
    r = elasticsearch_client.indices.get("*")  # get all indices
    for item in r:
        stats = elasticsearch_client.indices.stats(index=item)
        print(item, stats)
