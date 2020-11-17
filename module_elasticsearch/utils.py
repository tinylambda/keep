import json

from module_elasticsearch import elasticsearch_client


def print_return_result(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        args_string = ', '.join(map(str, args))
        kwargs_string = ', '.join([f'{k}={str(v)}' for k, v in kwargs.items()])
        all_args_string = ', '.join([args_string, kwargs_string])
        print(f'{f.__name__}({all_args_string}) >>> \n', json.dumps(r, indent=4), end='\n' * 2)
        return r
    return wrapper


@print_return_result
def cluster_health(c, **kwargs):
    r = c.cluster.health()
    return r


@print_return_result
def cluster_nodes(c, **kwargs):
    r = c.cat.nodes(**kwargs)
    return r


@print_return_result
def index_create(c, name, **kwargs):
    r = c.indices.create(name, **kwargs)
    return r


@print_return_result
def index_delete(c, name, **kwargs):
    r = c.indices.delete(name, **kwargs)
    return r


@print_return_result
def index_exists(c, name, **kwargs):
    r = c.indices.exists(name, **kwargs)
    return r


@print_return_result
def index_put_alias(c, name, alias_name, **kwargs):
    r = c.indices.put_alias(name, alias_name, **kwargs)
    return r


@print_return_result
def index_get_alias(c, name=None, alias_name=None, **kwargs):
    r = c.indices.get_alias(index=name, name=alias_name, **kwargs)
    return r


@print_return_result
def index_delete_alias(c, name, alias_name, **kwargs):
    r = c.indices.delete_alias(name, alias_name, **kwargs)
    return r


@print_return_result
def index_put_settings(c, name, setting_body, **kwargs):
    r = c.indices.put_settings(setting_body, index=name, **kwargs)
    return r


@print_return_result
def index_get_settings(c, name, **kwargs):
    r = c.indices.get_settings(index=name, **kwargs)
    return r


@print_return_result
def index_close(c, name, **kwargs):
    r = c.indices.close(name, **kwargs)
    return r


@print_return_result
def index_open(c, name, **kwargs):
    r = c.indices.open(name, **kwargs)
    return r


@print_return_result
def index_reindex(c, reindex_body, **kwargs):
    r = c.reindex(reindex_body, **kwargs)
    return r


@print_return_result
def index_refresh(c, name, **kwargs):
    r = c.indices.refresh(name, **kwargs)
    return r


@print_return_result
def index_flush(c, name, **kwargs):
    r = c.indices.flush(index=name, **kwargs)
    return r


@print_return_result
def index_forcemerge(c, name, **kwargs):
    r = c.indices.forcemerge(index=name, **kwargs)
    return r


@print_return_result
def index_put_mapping(c, name, mapping_body, **kwargs):
    r = c.indices.put_mapping(mapping_body, index=name, **kwargs)
    return r


@print_return_result
def index_get_mapping(c, name, **kwargs):
    r = c.indices.get_mapping(name, **kwargs)
    return r


@print_return_result
def index_shrink(c, origin, dest, body, **kwargs):
    r = c.indices.shrink(origin, dest, body=body, **kwargs)
    return r


@print_return_result
def doc_index(c, name, doc_body, **kwargs):
    r = c.index(index=name, body=doc_body, **kwargs)
    return r


@print_return_result
def doc_search(c, name, search_body=None, **kwargs):
    if search_body is None:
        search_body = {
            'query': {
                'match_all': {}
            }
        }
    r = c.search(index=name, body=search_body, **kwargs)
    return r


if __name__ == '__main__':
    cluster_health(elasticsearch_client)
    if not index_exists(elasticsearch_client, 'myindex'):
        index_create(elasticsearch_client, 'myindex')

