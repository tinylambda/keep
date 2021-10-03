import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


"""
If None (default), the __hash__ method is generated according how eq and frozen are set.

If both are True, attrs will generate a __hash__ for you.

If eq is True and frozen is False, __hash__ will be set to None, marking it unhashable (which it is).

If eq is False, __hash__ will be left untouched meaning the __hash__ method of the base class will be used 
(if base class is object, this means it will fall back to id-based hashing.).

Although not recommended, you can decide for yourself and force attrs to create one 
(e.g. if the class is immutable even though you didn’t freeze it programmatically) 
by passing True or not. Both of these cases are rather special and should be used carefully.
"""


@attr.s(eq=True, frozen=True)
class CompleteHashable:
    x = attr.ib()
    y = attr.ib()


@attr.s(eq=True, frozen=False)
class Unhashable:
    x = attr.ib()
    y = attr.ib()


@attr.s(eq=False)
class UseBaseHash:
    x = attr.ib()
    y = attr.ib()


@attr.s(hash=True, frozen=False)
class ForceHash:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    complete_hashable = CompleteHashable(100, 200)
    logging.info('%s', hash(complete_hashable))

    try:
        unhashable = Unhashable(100, 200)
        hash(unhashable)
    except TypeError as e:
        logging.warning('error', exc_info=e)

    use_base_hash = UseBaseHash(100, 200)
    logging.info('%s', hash(use_base_hash))

    force_hash = ForceHash(100, 200)
    logging.info('%s', hash(force_hash))
