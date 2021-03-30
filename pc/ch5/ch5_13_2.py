import os
import glob
import fnmatch


names = os.listdir('.')
print(names)

names = [
    name for name in os.listdir('.')
    if os.path.isfile(os.path.join('.', name))
]
print(names)


dirnames = [
    name for name in os.listdir('.')
    if os.path.isdir(os.path.join('.', name))
]
print(dirnames)

pyfiles = [
    name for name in os.listdir('.')
    if name.endswith('.py')
]
print(pyfiles)

pyfiles = glob.glob('./*.py')
print(pyfiles)

pyfiles = [
    name for name in os.listdir('.')
    if fnmatch.fnmatch(name, '*.py')
]
print(pyfiles)

