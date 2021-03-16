from module_redis import redis_client

redis_client.incr('mycounter', 1)
redis_client.getset('mycounter', '0')
print(
    redis_client.get('mycounter')
)

