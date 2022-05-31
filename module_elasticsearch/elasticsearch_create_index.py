import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME


if __name__ == "__main__":
    r = elasticsearch_client.indices.create(DEFAULT_INDEX_NAME)
    print(json.dumps(r, indent=4))
