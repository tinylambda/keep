from module_redis import redis_client


# Normally the OK code is immediately returned.
# Redis forks, the parent continues to serve the clients, the child saves the DB on disk then exits.
# An error is returned if there is already a background save running or if there is another non-background-save process
# running, specifically an in-progress AOF rewrite.
result = redis_client.bgsave()
print("bgsave: ", result)

result = redis_client.lastsave()
print("lastsave: ", result)

# Instruct Redis to start an Append Only File rewrite process.
# The rewrite will create a small optimized version of the current Append Only File.
result = redis_client.bgrewriteaof()
print("bgrewriteaof: ", result)
