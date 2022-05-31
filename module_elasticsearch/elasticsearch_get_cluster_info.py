import json

from elasticsearch import Elasticsearch
from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME


if __name__ == "__main__":
    info = Elasticsearch.info(elasticsearch_client)
    print(json.dumps(info, indent=4))
