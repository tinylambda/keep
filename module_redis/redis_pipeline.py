import redis

redis_client = redis.Redis(password='rpassword')

with redis_client.pipeline(transaction=True) as pipeline:
    pipeline.multi()
    pipeline.set('k1', 'x')
    pipeline.set('k2', 'y')
    pipeline.set('k3', 'z')
    results = pipeline.execute()
    print(results)

    pipeline.incr('k1')  # This call will fail, But the following 2 will successfully executed
    pipeline.set('k2', 'v2')
    pipeline.set('k3', 'v3')
    results = pipeline.execute(raise_on_error=False)  # Do not raise error
    print(results)

print('should be x: ', redis_client.get('k1'))  # will still be x
print('should be v3: ', redis_client.get('k3'))  # will be v3

# Yes, Redis do support multi-object API (update multiple keys in one operation), but this
# won't mean it has transaction semantics. Here, the command for some keys success, but fail
# for others, leaving the database in a partially updated state. This means it does not support
# the Atomicity in ACID

