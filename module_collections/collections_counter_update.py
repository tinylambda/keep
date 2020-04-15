import collections


c = collections.Counter()
print('Initial: ', c)

c.update('abcdaab')
print('Sequence: ', c)

c.update({
    'a': 1,
    'd': 5
})  # The count values are increased based on the new data, rather than replaced.
print('Dict: ', c)



