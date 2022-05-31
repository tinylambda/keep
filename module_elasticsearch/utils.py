import json
import contextlib

from module_elasticsearch import elasticsearch_client


def print_return_result(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        args_string = ", ".join(map(str, args))
        kwargs_string = ", ".join([f"{k}={str(v)}" for k, v in kwargs.items()])
        all_args_string = ", ".join([args_string, kwargs_string])
        print(
            f"{f.__name__}({all_args_string}) >>> \n",
            json.dumps(r, indent=4),
            end="\n" * 2,
        )
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
def index_list(c, **kwargs):
    r = c.indices.get("*")
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
def index_alias_exists(c, name, index=None, **kwargs):
    r = c.indices.exists_alias(name, index=index, **kwargs)
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
def index_rollover(c, alias_name, body=None, new_index=None, **kwargs):
    r = c.indices.rollover(alias_name, body=body, new_index=new_index)
    return r


@print_return_result
def doc_index(c, name, doc_body, **kwargs):
    r = c.index(index=name, body=doc_body, **kwargs)
    return r


@print_return_result
def doc_get(c, name, id_, **kwargs):
    r = c.get(name, id_, **kwargs)
    return r


@print_return_result
def doc_get_source(c, name, id_, **kwargs):
    r = c.get_source(name, id_, **kwargs)
    return r


@print_return_result
def doc_exists(c, name, id_, **kwargs):
    r = c.exists(name, id_, **kwargs)
    return r


@print_return_result
def doc_delete(c, name, id_, **kwargs):
    r = c.delete(name, id_, **kwargs)
    return r


@print_return_result
def doc_update(c, name, id_, update_body, **kwargs):
    r = c.update(name, id_, update_body, **kwargs)
    return r


@print_return_result
def doc_bulk(c, bulk_body, **kwargs):
    r = c.bulk(bulk_body, **kwargs)
    return r


@print_return_result
def doc_mget(c, mget_body, **kwargs):
    r = c.mget(mget_body, **kwargs)
    return r


DEFAULT_SEARCH_BODY_WITH_SNPT = {
    "seq_no_primary_term": True,
    "query": {"match_all": {}},
}

DEFAULT_SEARCH_BODY = {"query": {"match_all": {}}}


@print_return_result
def doc_search(c, name, search_body=DEFAULT_SEARCH_BODY_WITH_SNPT, **kwargs):
    r = c.search(index=name, body=search_body, **kwargs)
    return r


@print_return_result
def doc_count(c, name, search_body=DEFAULT_SEARCH_BODY, **kwargs):
    r = c.count(index=name, body=search_body, **kwargs)
    return r


@print_return_result
def doc_explain(c, name, id_, search_body=None, **kwargs):
    r = c.explain(index=name, id=id_, body=search_body, **kwargs)
    return r


@contextlib.contextmanager
def testing_index(c, index_name, **kwargs):
    """
    :param c: The Elasticsearch Client to use
    :param index_name: The index's name to test
    :return: None
    """
    # We first create a index named `index_name`
    if index_exists(c, index_name):
        index_delete(c, index_name)
    index_create(c, index_name, **kwargs)
    try:
        yield
    finally:
        # finally we delete the index for testing
        index_delete(c, index_name)


if __name__ == "__main__":
    cluster_health(elasticsearch_client)
    if not index_exists(elasticsearch_client, "myindex"):
        index_create(elasticsearch_client, "myindex")
