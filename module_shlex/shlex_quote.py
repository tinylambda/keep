import shlex

examples = [
    "embedded'singlequote",
    'embedded"doublequote',
    "embedded space",
    "~SpecialCharacter",
    r"Back\slash",
]

for s in examples:
    print("original: {}".format(s))
    print("quote: {}".format(shlex.quote(s)))
    print()
