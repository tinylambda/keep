import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class MetaClass(type):
    META_VAR = 'EEE'

    def meta_test(cls):
        logging.info('meta.meta_test cls: %s; meta.meta_property=%s; cls.__class__.META_VAR=%s',
                     cls, cls.meta_property, cls.__class__.META_VAR)

    @property
    def meta_property(cls):
        logging.info('meta.meta_property cls: %s', cls)
        return 10000

    def __new__(mcs, clsname, bases, class_dict: dict):
        logging.info('meta.__new__.mcs is : %s (%s)', mcs, id(mcs))
        # create the CLASS
        cls = type.__new__(mcs, clsname, bases, class_dict)
        logging.info('meta.__new__.cls is : %s (%s)', cls, id(cls))
        return cls

    def __init__(cls, clsname, bases, class_dict: dict):
        # initialization at class level
        cls.A = []
        logging.info('meta.__init__.cls is: %s (%s); cls.__class__: %s (%s)',
                     cls, id(cls), cls.__class__, id(cls.__class__))
        cls.meta_test()
        super(MetaClass, cls).__init__(clsname, bases, class_dict)


class Base(metaclass=MetaClass):
    @classmethod
    def test(cls):
        logging.info('Base.cls is : %s (%s), cls.A: %s (%s)', cls, id(cls), cls.A, id(cls.A))
        logging.info('%s', cls.__class__.META_VAR)


class B1(Base):
    pass


class B2(Base):
    pass


if __name__ == '__main__':
    logging.info('B1.A: %s (%s)', B1.A, id(B1.A))
    logging.info('B2.A: %s (%s)', B2.A, id(B2.A))

    B1.test()
    B2.test()
