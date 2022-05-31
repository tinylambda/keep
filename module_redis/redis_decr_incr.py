from module_redis import redis_client


KEY = "KEY_FOR_DECR_INCR"
print("Initial value: ", redis_client.get(KEY))

redis_client.incr(KEY)  # If key not exists, will be initialized to 0 first
print("Result after incr: ", redis_client.get(KEY))

redis_client.decr(KEY)
print("Result after decr: ", redis_client.get(KEY))
