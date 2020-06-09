from module_redis import redis_client

KEY = 'test_key'
VALUE = 'test_value'
print('set {} = {}'.format(KEY, VALUE))
redis_client.set(KEY, VALUE)

print('get {}'.format(KEY))
value = redis_client.get(KEY)
print('{} = {}'.format(KEY, value))

print('del {}'.format(KEY))
redis_client.delete(KEY)
print('get {} after deleting it'.format(KEY))
value = redis_client.get(KEY)
print('{} = {}'.format(KEY, value))

