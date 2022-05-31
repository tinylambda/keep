import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


# Instead of setting the init, repr, eq, order, and hash arguments explicitly,
# assume they are set to True unless any of the involved methods for one of the arguments is implemented in the current
# class (i.e. it is not inherited from some base class).
@attr.s(auto_detect=True)
class C:
    x = attr.ib(type=int)
    y = attr.ib(type=int)

    # So for example by implementing __eq__ on a class yourself, attrs will deduce eq=False and will create neither
    # __eq__ nor __ne__ (but Python classes come with a sensible __ne__ by default, so it should be enough to only
    # implement __eq__ in most cases).
    def __eq__(self, other):
        return self.x == other.x


if __name__ == "__main__":
    c1 = C(100, 200)
    c2 = C(100, 300)
    logging.info("%s", c1 == c2)
    logging.info("%s", c1 != c2)
