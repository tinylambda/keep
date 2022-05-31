import elasticsearch


DEFAULT_INDEX_NAME = "test"
CUSTOMER_INDEX_NAME = "customer"
INDEX_FOR_TESTING_TEMPLATE = "index_template"


elasticsearch_client = elasticsearch.Elasticsearch(
    hosts=[{"host": "127.0.0.1", "port": 9200}]
)
