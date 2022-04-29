from enum import Enum


class ProjectPaymentStatus(bytes, Enum):
    def __new__(cls, value, text):
        print('Constructing', cls, type(cls))
        obj = bytes.__new__(cls, [value])
        print(type(obj))
        obj._value_ = value
        obj.text = text
        obj.full = (value, text)
        return obj

    not_update = (0, 'Not Update')
    payment_required = (1, 'Required')
    payment_processing = (2, 'Processing')
    payment_received = (3, 'Succeeded')


if __name__ == '__main__':
    a = ProjectPaymentStatus.payment_processing
    print(a)
    print(a.value)
    print(type(a), type(a.full))
