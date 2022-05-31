from module_elasticsearch import elasticsearch_client
from module_elasticsearch import DEFAULT_INDEX_NAME


if __name__ == "__main__":
    r = elasticsearch_client.indices.put_mapping(
        {
            "properties": {
                "email": {"type": "keyword"},
                "name": {"type": "keyword"},
                "tag": {"type": "keyword", "store": "true"},
                "item": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "text"},
                        "quantity": {"type": "integer"},
                        "price": {"type": "double"},
                        "vat": {"type": "double"},
                    },
                },
            }
        },
        index=DEFAULT_INDEX_NAME,
    )

    print(r)
