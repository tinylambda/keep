import time

from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_ip'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'ip': {'type': 'ip'}
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'ip': 'fe80::c633:e480:2465:3642',  # ipv4/6 ip address
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME)

    index_delete(elasticsearch_client, INDEX_NAME)

