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

INDEX_NAME = 'index_for_test'

# The completion suggester provides auto-complete/search-as-you-type functionality. This is a navigational feature to
# guide users to relevant results as they are typing, improving search precision.
# It is not meant for spell correction or did-you-mean functionality like the term or phrase suggesters.
# #

if __name__ == '__main__':
    if index_exists(elasticsearch_client, INDEX_NAME):
        index_delete(elasticsearch_client, INDEX_NAME)

    index_create(elasticsearch_client, INDEX_NAME)
    mapping_body = {
        'properties': {
            'suggest': {
                'type': 'completion',
                'analyzer': 'simple',
                'search_analyzer': 'simple',
                'preserve_separators': True,
                'max_input_length': 50,
            },
            'title': {
                'type': 'keyword'
            }
        }
    }
    index_put_mapping(elasticsearch_client, INDEX_NAME, mapping_body)
    index_get_mapping(elasticsearch_client, INDEX_NAME)

    doc_body = {
        'suggest': {
            'input': ['ES', 'Elasticsearch', 'Elastic Search', 'Elasticsearch Cookbook'],
            'weight': 34
        }
    }
    doc_index(elasticsearch_client, INDEX_NAME, doc_body)
    time.sleep(1)
    doc_search(elasticsearch_client, INDEX_NAME, search_body={
        'suggest': {
            'book-suggest': {
                'prefix': 'EL',
                'completion': {
                    'field': 'suggest',
                }
            }
        }
    })

    index_delete(elasticsearch_client, INDEX_NAME)

