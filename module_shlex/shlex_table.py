import shlex

text = """|Col 1||Col2||Col 3|"""
print("original: {!r}".format(text))
print()

lexer = shlex.shlex(text)
lexer.quotes = "|"

print("tokens:")
for token in lexer:
    print("{!r}".format(token))
