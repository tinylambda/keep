import collections


c = collections.Counter("extremely")
c["z"] = 0
print(c)
print(
    list(c.elements())
)  # The order of elements is not guaranteed, and items with counts less \
# than or equal to zero are not included.
