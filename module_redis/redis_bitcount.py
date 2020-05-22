from module_redis import redis_client


KEY = 'bitcount_key'
redis_client.set(KEY, 'foobar')
# Count the number of set bits (population counting) in a string
result = redis_client.bitcount(KEY)
print('bitcount: ', result)

