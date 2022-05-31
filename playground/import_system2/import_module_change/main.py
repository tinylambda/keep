from small import x, y


x = 42
y[0] = 42

import small

print(small.x)
print(small.y)

small.x = 42
print(small.x)
