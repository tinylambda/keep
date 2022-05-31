from module_redis import redis_client

redis_client.set("name", "Felix")

script = """
local val="Hello world"
return val
"""
ret = redis_client.eval(script, 0)
print(ret)

script = """
return ARGV[1]..' '..KEYS[1]
"""
ret = redis_client.eval(script, 2, *["name", "k2", "Hello", "arg2", "arg3"])
print(ret)

script = """
return ARGV[1].." "..redis.call("get", KEYS[1]) 
"""
ret = redis_client.eval(script, 2, *["name", "k2", "Hello", "arg2", "arg3"])
print(ret)

script = """
local name=redis.call("get", KEYS[1])
local greet=ARGV[1]
local result=greet..' '..name
return result
"""
ret = redis_client.eval(script, 2, *["name", "k2", "Hello", "arg2", "arg3"])
print(ret)

redis_client.rpush("region:one", "count: emea", "count:usa", "count:atlantic")
redis_client.rpush("region:two", "count:usa")
script = """
local count=0
local broadcast=redis.call("LRANGE", KEYS[1], 0, -1)
for _, key in ipairs(broadcast) do
    redis.call("INCR", key)
    count=count+1
end
return count
"""
script_sha = redis_client.script_load(script=script)

# ret = redis_client.eval(script, 1, *['region:one'])
# print(ret)
#
# ret = redis_client.eval(script, 1, *['region:two'])
# print(ret)

ret = redis_client.evalsha(script_sha, 1, *["region:one"])
print(ret)

ret = redis_client.evalsha(script_sha, 1, *["region:two"])
print(ret)

ret = redis_client.mget(["count: emea", "count:usa", "count:atlantic"])
print(ret)

redis_client.delete(
    *["region:one", "region:two", "count: emea", "count:usa", "count:atlantic"]
)
