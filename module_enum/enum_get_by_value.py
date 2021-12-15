import enum

CACHE_CODE_TO_CATEGORY: dict = {}


class Category(enum.Enum):
    HISTORY = {
        'code': 10001,
        'name': 'history',
    }
    MATH = {
        'code': 10002,
        'name': 'math',
    }
    PHYSICS = {
        'code': 10003,
        'name': 'physics',
    }

    def __init__(self, value: dict):
        self.code = value['code']
        self.category_name = value['name']
        CACHE_CODE_TO_CATEGORY[self.code] = self

    @classmethod
    def get_by_code(cls, code: int):
        return CACHE_CODE_TO_CATEGORY.get(code)


if __name__ == '__main__':
    print(Category.get_by_code(10001))
    print(Category.get_by_code(10002))

