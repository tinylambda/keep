import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import (
    DEFAULT_INDEX_NAME,
    CUSTOMER_INDEX_NAME,
    INDEX_FOR_TESTING_TEMPLATE,
)


if __name__ == "__main__":
    mapping_info = elasticsearch_client.indices.get_mapping(INDEX_FOR_TESTING_TEMPLATE)
    print(json.dumps(mapping_info, indent=4))
