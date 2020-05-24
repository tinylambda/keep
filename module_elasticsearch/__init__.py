import elasticsearch


DEFAULT_INDEX_NAME = 'default'


elasticsearch_client = elasticsearch.Elasticsearch(hosts=[{"host": "localhost", "port": 9200}])

