from enum import Enum


class ProjectLaborType(bytes, Enum):
    def __new__(cls, value, text):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.text = text
        obj.full = (value, text)
        return obj

    Flooring = (1, 'Flooring')


PROJECT_LABOR_TYPE_MAP = dict([o.full for o in ProjectLaborType])
PROJECT_LABOR_TYPE_MAP_REVERSE = dict([(o.text, o.value) for o in ProjectLaborType])


if __name__ == '__main__':
    print(PROJECT_LABOR_TYPE_MAP)
    print(PROJECT_LABOR_TYPE_MAP_REVERSE)
