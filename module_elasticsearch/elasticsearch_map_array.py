import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME, CUSTOMER_INDEX_NAME


if __name__ == '__main__':
    r = elasticsearch_client.search(index=DEFAULT_INDEX_NAME, body={
        'query': {
            'match_all': {}
        }
    })
    print(json.dumps(r, indent=4))

