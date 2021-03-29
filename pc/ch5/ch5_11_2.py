import os

path = '/Users/Felix/PycharmProjects/keep/requirements.txt'

print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/data/data.csv'
print(os.path.expanduser(path))
print(os.path.splitext(path))


