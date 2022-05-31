from module_redis import redis_client

# The SCAN command and the closely related commands SSCAN, HSCAN and ZSCAN are used in order to
# incrementally iterate over a collection of elements
# SCAN: iterates the set of keys in the currently selected Redis database.


def do_scan(match=None, _type=None):
    print(f"Scan with match={match} and _type={_type}")
    next_cursor = 0
    counter = 0
    while True:
        # the MATCH filter is applied after elements are retrieved from the collection, just before returning
        # data to the client. This means that if the pattern matches very little elements inside the collection,
        # SCAN will likely return no elements in most iterations.
        next_cursor, keys = redis_client.scan(next_cursor, match=match, _type=_type)
        for key in keys:
            # print(key)
            counter += 1

        if next_cursor == 0:
            break

    print(counter, end="\n\n")


do_scan()
do_scan(match="key_*")

info = redis_client.info("Server")

if info.get("redis_version") >= "6.0.0":
    do_scan(_type="ZSET")
