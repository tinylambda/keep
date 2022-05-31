import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME, INDEX_FOR_TESTING_TEMPLATE


if __name__ == "__main__":
    r = elasticsearch_client.indices.delete(INDEX_FOR_TESTING_TEMPLATE)
    print(json.dumps(r, indent=4))
