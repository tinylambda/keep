import pathlib


p = pathlib.Path('..')

print(p.resolve())
for f in p.rglob('pathlib_*.py'):
    print(f)
