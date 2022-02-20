from pydantic import BaseModel, StrictBytes, ValidationError, StrictInt, confloat, StrictBool


class StrictBytesModel(BaseModel):
    strict_bytes: StrictBytes
    normal_bytes: bytes


class StrictIntModel(BaseModel):
    strict_int: StrictInt
    normal_int: int


class ConstrainedFloatModel(BaseModel):
    constrained_float: confloat(strict=True, ge=0.0)


class StrictBoolModel(BaseModel):
    strict_bool: StrictBool
    normal_bool: bool


if __name__ == '__main__':
    try:
        m = StrictBytesModel(strict_bytes='hello world', normal_bytes='hello world')
    except ValidationError as e:
        print(e)

    try:
        m = StrictIntModel(strict_int=3.14, normal_int=3.14)
    except ValidationError as e:
        print(e)

    try:
        m = ConstrainedFloatModel(constrained_float=3)
    except ValidationError as e:
        print(e)

    try:
        m = ConstrainedFloatModel(constrained_float=-3.14)
    except ValidationError as e:
        print(e)

    try:
        m = StrictBoolModel(strict_bool='False', normal_bool='False')
    except ValidationError as e:
        print(e)
