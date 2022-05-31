import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()


# the correct way to archive hashing by id is to set @attr.s(eq=False).
@attr.s(eq=False)
class HashableById:
    x = attr.ib()


@attr.s(frozen=True)
class HashableByValues:
    x = attr.ib()


# Beware, however, that this is not a complete guarantee of safety:
# if a field points to an object and that object is mutated, the hash code may change, but frozen will not protect you.
@attr.s(frozen=True)
class HashableC:
    x = attr.ib()
    y = attr.ib(default=attr.Factory(lambda: HashableById(100)))


@attr.s(frozen=True)
class HashableC2:
    x = attr.ib()
    y = attr.ib(default=attr.Factory(lambda: HashableByValues(100)))


if __name__ == "__main__":
    c = C(100)
    try:
        logging.info("%s", hash(c))
    except TypeError as e:
        logging.warning("hash error", exc_info=e)

    hashable_c = HashableC(100)
    hashable_c_2 = HashableC(100)

    # y is different object, hash of the two should not be equal
    logging.info("HashableC: %s", hash(hashable_c))
    logging.info("HashableC: %s", hash(hashable_c_2))
    logging.info("%s", hashable_c == hashable_c_2)

    logging.info("%s", "*" * 64)
    hashable_c2 = HashableC2(100)
    hashable_c2_2 = HashableC2(100)
    logging.info("HashableC2: %s", hash(hashable_c2))
    logging.info("HashableC2: %s", hash(hashable_c2_2))
    logging.info("%s", hashable_c2 == hashable_c2_2)  # True

    logging.info("%s", "*" * 64)
    hash_by_id = HashableById(100)
    hash_by_id_2 = HashableById(100)
    # hashing by object id, obviously hash value of the two objects are not equal
    logging.info("HashableById: %s", hash(hash_by_id))
    logging.info("HashableById: %s", hash(hash_by_id_2))
    logging.info("%s", hash_by_id == hash_by_id_2)  # False
