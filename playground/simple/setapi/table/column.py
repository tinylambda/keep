import attr

from playground.simple.setapi.table.sqltype import SqlType


@attr.s
class Column:
    name = attr.ib(type=str)
    type = attr.ib(type=SqlType)
    partition_column = attr.ib(type=bool, default=False)
    desc = attr.ib(type=str, default="")
    extra = attr.ib(type=dict, default=attr.Factory(dict))

    def is_number_column(self):
        return self.type.is_number

    def is_float_column(self):
        return self.type.is_float
