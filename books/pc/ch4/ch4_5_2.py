a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

f = open('/etc/passwd')
for line in reversed(list(f)):
    print(line, end='')

