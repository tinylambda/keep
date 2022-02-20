import re
from pprint import pprint
from typing import Optional

from pydantic import BaseModel

post_code_regex = re.compile(
    r'(?:'
    r'([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?'
    r'([0-9][A-Z]{2})|'
    r'(BFPO) ?([0-9]{1,4})|'
    r'(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|'
    r'([A-Z]{2}) ?([0-9]{2})|'
    r'(GE) ?(CX)|'
    r'(GIR) ?(0A{2})|'
    r'(SAN) ?(TA1)'
    r')'
)


class PostCode(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError('string required')
        m = post_code_regex.fullmatch(v.upper())
        if not m:
            raise ValueError('invalid postcode format')
        return cls(f'{m.group(1)} {m.group(2)}')

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            pattern='^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$',
            examples=['SP11 9DG', 'w1j7bu'],
        )

    def __repr__(self):
        return f'PostCode({super().__repr__()})'


class Model(BaseModel):
    post_code: PostCode
    good_int: Optional[int]


if __name__ == '__main__':
    m = Model(post_code='sw8 5el')
    print(m)
    print(m.post_code)
    pprint(Model.schema())
