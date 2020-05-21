import time
import threading
import redis


redis_client = redis.Redis(password='rpassword')

redis_client.set('balance', 100)


def increment_balance(r):
    print('Change balance')
    r.incr('balance')


# transaction = True will put wrap commands between MULTI and EXEC block
START = True
with redis_client.pipeline(transaction=True) as pipeline:
    while True:
        try:
            pipeline.watch('balance')

            if START:
                # other thread to change balance
                t = threading.Thread(target=increment_balance, args=(redis_client, ))
                t.setDaemon(True)
                t.start()

            print('Work for 5 seconds to earn more money.')
            time.sleep(5)

            current_balance = pipeline.get('balance')
            new_balance = int(current_balance) + 10
            pipeline.multi()
            pipeline.set('new_key', 'new_value')
            pipeline.set('balance', new_balance)
            pipeline.execute()
            break
        except redis.WatchError:
            print('Another thread change the balance! retry')
            START = False
            continue

print('Final result should be 111: ', redis_client.get('balance'))
