import logging
import sys
import typing
from typing import List, AnyStr

import attr

from playground.simple.setapi.table.column import Column
from playground.simple.setapi.table.sqltype import SqlType

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Table:
    name = attr.ib(eq=True)
    desc = attr.ib(eq=False)
    columns = attr.ib(type=List[Column], eq=False)

    column_dict = attr.ib(
        type=typing.Dict[AnyStr, Column],
        init=False,
        default=attr.Factory(dict),
        eq=False,
    )

    def __attrs_post_init__(self):
        for column in self.columns:
            self.column_dict.update({column.name: column})

    def get_column(self, column_name: str) -> Column:
        return self.column_dict[column_name]

    def has_column(self, column: Column) -> bool:
        try:
            if self.get_column(column.name) is not None:
                return True
        except KeyError:
            pass
        return False


if __name__ == "__main__":
    table = Table(
        "test_table",
        "this is a good table",
        columns=[
            Column("col1", SqlType.string, "this is a good column"),
            Column("col2", SqlType.int, "this is also a good column"),
            Column("col3", SqlType.float, "this is also a good column"),
        ],
    )

    logging.info("%s", table)
    for _column in table.columns:
        logging.info("%s", _column.is_number_column())
        logging.info("%s", _column.is_float_column())
