from decimal import Decimal

from pydantic import BaseModel, conbytes, constr, conint, PositiveInt, NegativeInt, NonNegativeInt, NonPositiveInt, \
    confloat, PositiveFloat, NegativeFloat, NonNegativeFloat, NonPositiveFloat, conlist, conset, condecimal, Field


class Model(BaseModel):
    lower_bytes: conbytes(to_lower=True)
    short_bytes: conbytes(min_length=2, max_length=10)
    strip_bytes: conbytes(strip_whitespace=True)

    lower_str: constr(to_lower=True)
    short_str: constr(min_length=2, max_length=10)
    regex_str: constr(regex=r'^apple (pie|tart|sandwich)$')
    strip_str: constr(strip_whitespace=True)

    big_int: conint(gt=1000, lt=1024)
    mod_int: conint(multiple_of=5)
    pos_int: PositiveInt
    neg_int: NegativeInt
    non_neg_int: NonNegativeInt
    non_pos_int: NonPositiveInt

    big_float: confloat(gt=1000, lt=1024)
    unit_interval: confloat(ge=0, le=1)
    mod_float: confloat(multiple_of=0.5)
    pos_float: PositiveFloat
    neg_float: NegativeFloat
    non_neg_float: NonNegativeFloat
    non_pos_float: NonPositiveFloat

    short_list: conlist(int, min_items=1, max_items=4)
    short_set: conset(int, min_items=1, max_items=4)

    decimal_positive: condecimal(gt=0)
    decimal_negative: condecimal(lt=0)
    decimal_max_digits_and_places: condecimal(max_digits=2, decimal_places=2)
    mod_decimal: condecimal(multiple_of=Decimal('0.25'))

    bigger_int: int = Field(..., gt=10000)


if __name__ == '__main__':
    m = Model(
        lower_bytes=b'ABC',
        short_bytes=b'AB',
        strip_bytes=b' abcd123 ',
        lower_str='ABC',
        short_str='ab',
        regex_str='apple tart',
        strip_str='  hello world  ',
        big_int=1001,
        mod_int=-15,
        pos_int=1,
        neg_int=-1,
        non_neg_int=0,
        non_pos_int=0,
        big_float=1001,
        unit_interval=0.001,
        mod_float=1.5,
        pos_float=0.11,
        neg_float=-0.1,
        non_pos_float=0.0,
        non_neg_float=0.0,
        short_list=[1, 2],
        short_set=[1, 2, 3, 3],
        decimal_positive=0.1,
        decimal_negative=-0.11,
        decimal_max_digits_and_places=0.11,
        mod_decimal=0.50,
        bigger_int=10000000,
    )
    print(m)
