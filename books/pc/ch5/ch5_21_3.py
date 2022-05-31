import pickle

f = open("/tmp/data", "wb")
pickle.dump([1, 2, 3, 4], f)
pickle.dump("hello", f)
pickle.dump({"apple", "pear", "banana"}, f)
f.close()

f = open("/tmp/data", "rb")
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()

import math

print(pickle.dumps(math.cos))
