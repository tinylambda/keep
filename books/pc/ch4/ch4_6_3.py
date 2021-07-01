from ch4_6_2 import LineHistory


f = open('/etc/passwd')
lines = LineHistory(f)

it = iter(lines)
print(
    next(it)
)
print(
    next(it)
)
f.close()

