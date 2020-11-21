import time

from module_elasticsearch.utils import testing_index
from module_elasticsearch.utils import \
    index_create, \
    index_delete, \
    index_exists, \
    index_put_mapping, \
    index_get_mapping, \
    doc_index, \
    doc_search, cluster_nodes, cluster_health, \
    index_put_settings, index_get_settings, \
    index_shrink, index_put_alias, index_get_alias,\
    index_delete_alias, index_rollover, index_list, \
    index_refresh, index_alias_exists, doc_get, doc_exists, doc_get_source, doc_delete, doc_update
from module_elasticsearch import elasticsearch_client

INDEX_NAME = 'index_for_test'


if __name__ == '__main__':
    with testing_index(elasticsearch_client, INDEX_NAME):
        doc_id = '1'
        doc_body = {
            'counter': 1,
            'tags': ['red']
        }
        # refresh=True for testing
        doc_index(elasticsearch_client, INDEX_NAME, doc_body=doc_body, id=doc_id, refresh=True)
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)
        # Now update this doc
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': 'ctx._source.counter += params.count',
                'lang': 'painless',
                'params': {
                    'count': 4
                }
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # another update
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': 'ctx._source.tags.add(params.tag)',
                'lang': 'painless',
                'params': {
                    'tag': 'blue'
                }
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # another update
        script_source = 'if (ctx._source.tags.contains(params.tag)) ' \
                        '{ ctx._source.tags.remove(ctx._source.tags.indexOf(params.tag)) }'
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': script_source,
                'lang': 'painless',
                'params': {
                    'tag': 'blue'
                }
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # add new field
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': 'ctx._source.new_field = "value of new field"',
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # remove a field
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': 'ctx._source.remove("new_field")'
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # replace op
        script_source = 'if (ctx._source.tags.contains(params.tag)) {ctx.op = "delete"} else {ctx.op = "none"}'
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'script': {
                'source': script_source,
                'params': {
                    'tag': 'green'  # change to red to delete the doc
                }
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # update part of a document, if both doc and script a specified, then doc is ignored
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'doc': {
                'name': 'new_name',
            }
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # if value not change, return noop
        doc_update(elasticsearch_client, INDEX_NAME, doc_id, update_body={
            'doc': {
                'name': 'new_name',
            },
            'detect_noop': False,
        })
        doc_get(elasticsearch_client, INDEX_NAME, doc_id)

        # if doc not exists, the contents of upsert element are inserted as a new document else execute script
        temp_id = 2
        doc_update(elasticsearch_client, INDEX_NAME, temp_id, update_body={
            'script': {
                'source': 'ctx._source.counter += params.count',
                'lang': 'painless',
                'params': {
                    'count': 4
                }
            },
            'upsert': {
                'counter': 1
            },
            'scripted_upsert': True,  # execute script after upsert op
        })
        doc_get(elasticsearch_client, INDEX_NAME, temp_id)

        # doc as upsert
        temp_id = 3
        doc_update(elasticsearch_client, INDEX_NAME, temp_id, update_body={
            'doc': {
                'name': 'new_name'
            },
            'doc_as_upsert': True,
        })
        doc_get(elasticsearch_client, INDEX_NAME, temp_id)

