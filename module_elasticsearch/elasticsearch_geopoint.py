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

INDEX_NAME = 'index_for_geopoint'


if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'id': {'type': 'keyword'},
            'date': {'type': 'date'},
            'customer_id': {'type': 'keyword'},
            'customer_ip': {'type': 'ip'},
            'customer_location': {'type': 'geo_point'},
            'sent': {'type': 'boolean'},
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'customer_location': {
            'lat': 45.61752,
            'lon': 9.08363
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    search_body = {
        '_source': ['customer_location'],
        'query': {
            'match_all': {}
        }
    }
    doc_search(elasticsearch_client, INDEX_NAME, search_body=search_body)

    index_delete(elasticsearch_client, INDEX_NAME)

