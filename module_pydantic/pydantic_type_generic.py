from typing import TypeVar, Generic

from pydantic import ValidationError, BaseModel
from pydantic.fields import ModelField

AgedType = TypeVar("AgedType")
QualityType = TypeVar("QualityType")


class TastingModel(Generic[AgedType, QualityType]):
    def __init__(self, name: str, aged: AgedType, quality: QualityType):
        self.name = name
        self.aged = aged
        self.quality = quality

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field: ModelField):
        if not isinstance(v, cls):
            raise TypeError("Invalid value")
        if not field.sub_fields:
            return v
        aged_f = field.sub_fields[0]
        quality_f = field.sub_fields[1]
        errors = []

        valid_value, error = aged_f.validate(v.aged, {}, loc="aged")
        if error:
            errors.append(error)

        valid_value, error = quality_f.validate(v.quality, {}, loc="quality")
        if error:
            errors.append(error)

        if errors:
            raise ValidationError(errors, cls)
        return v


class Model(BaseModel):
    wine: TastingModel[int, float]
    cheese: TastingModel[bool, str]
    thing: TastingModel


if __name__ == "__main__":
    m = Model(
        wine=TastingModel(name="Cabernet Sauvignon", aged=20, quality=85.6),
        cheese=TastingModel(name="Gouda", aged=True, quality="Good"),
        thing=TastingModel(name="Python", aged="not much", quality="Awesome"),
    )
    print(m)
    print(m.wine.aged)
    print(m.wine.quality)

    print(m.cheese.aged)
    print(m.cheese.quality)

    print(m.thing.aged)

    try:
        Model(
            wine=TastingModel(name="Merlot", aged=True, quality="Kinda good"),
            cheese=TastingModel(name="Gouda", aged="yeah", quality=5),
            thing=TastingModel(name="Python", aged="not much", quality="Awesome"),
        )
    except ValidationError as e:
        print(e)
