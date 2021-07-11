import shlex

text = """This text has "quoted parts" inside it."""
print('original: {!r}'.format(text))
print()

print('tokens:')
print(shlex.split(text))

