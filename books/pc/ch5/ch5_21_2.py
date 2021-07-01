import pickle

data = [1, 2, 3]
# serialized to file
f = open('/tmp/data', 'wb')
pickle.dump(data, f)
f.close()

# serialized to str
serialized = pickle.dumps(data)
print(serialized)

# deserialized from file
f = open('/tmp/data', 'rb')
deserialized = pickle.load(f)
print(deserialized)

# deserialized from str
deserialized = pickle.loads(serialized)
print(deserialized)

