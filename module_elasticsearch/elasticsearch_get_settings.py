import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME


if __name__ == '__main__':
    settings_info = elasticsearch_client.indices.get_settings(index=DEFAULT_INDEX_NAME)
    print(json.dumps(settings_info, indent=4))

