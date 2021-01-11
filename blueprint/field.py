import typing


class Field:
    def __init__(
            self,
            verbose_name: typing.AnyStr = None,
            data_type: typing.Any = 'string',
            required: bool = True,
            default: typing.Any = None,
            multi: bool = False,
    ):
        self.name = None
        self.fullname = None
        self.internal_name = None
        self.verbose_name: typing.AnyStr = verbose_name
        self.data_type: typing.AnyStr = data_type
        self.required: bool = required
        self.default: typing.Any = default
        self.multi: bool = multi

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = getattr(instance, self.internal_name, None)
        value = value if value else self.default
        return value

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

