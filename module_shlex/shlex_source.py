import shlex


text = "This text says to source quotes.txt before continuing."
print("original: {!r}".format(text))
print()


lexer = shlex.shlex(text)
lexer.wordchars += "."
lexer.source = "source"

print("tokens:")
for token in lexer:
    print("{!r}".format(token))
