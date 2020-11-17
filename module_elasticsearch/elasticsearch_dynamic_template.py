import json

from module_elasticsearch import elasticsearch_client
from module_elasticsearch import INDEX_FOR_TESTING_TEMPLATE


if __name__ == '__main__':
    # # Create index
    # r = elasticsearch_client.indices.create(INDEX_FOR_TESTING_TEMPLATE)
    # print(json.dumps(r, indent=4))

    # # Put dynamic templates
    # r = elasticsearch_client.indices.put_mapping(
    #     {
    #         'dynamic_date_formats': ['yyyy-MM-dd', 'dd-MM-yyyy'],
    #         'date_detection': True,
    #         'numeric_detection': True,
    #         'dynamic_templates': [
    #             {
    #                 'template1': {
    #                     'match': '*',
    #                     'match_mapping_type': 'long',
    #                     'mapping': {
    #                         'type': '{dynamic_type}',
    #                         'store': True
    #                     }
    #                 }
    #             }
    #         ],
    #         'properties': {
    #
    #         }
    #     },
    #    index=INDEX_FOR_TESTING_TEMPLATE,
    # )
    # print(json.dumps(r, indent=4))

    doc = {
        'name': 'Mate 40 Pro 5G RS Design',
        'number': 17686554,
        'ds': '2020-11-11',
        's2': '11-11-2020',
        'more': 1,
    }
    elasticsearch_client.index(INDEX_FOR_TESTING_TEMPLATE, body=doc)

    # r = elasticsearch_client.indices.put_mapping(body={
    #     'dynamic_date_formats': ['yyyy-MM-dd', 'dd-MM-yyyy'],
    #     'dynamic_templates': [
    #         {
    #             'store_generic_template': {
    #                 'match': '*',
    #                 'mapping': {
    #                     'store': True
    #                 }
    #             }
    #         }
    #     ]
    # }, index=INDEX_FOR_TESTING_TEMPLATE)
    # print(json.dumps(r, indent=4))





