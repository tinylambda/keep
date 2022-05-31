import re
from typing import Dict, List

import attr

from playground.simple.setapi import SetApi
from playground.simple.setapi.table.column import Column
from playground.simple.setapi.table.sqltype import SqlType
from playground.simple.setapi.table.table import Table


@attr.s
class SqlSet(SetApi):
    name = attr.ib(type=str, eq=True)
    desc = attr.ib(type=str, eq=False)
    base_table = attr.ib(type=Table, eq=False)
    key_column = attr.ib(type=Column, eq=False)
    read_filter = attr.ib(type=List[List[Dict]], eq=False)
    write_filter = attr.ib(type=List[List[Dict]], eq=False)

    def __attrs_post_init__(self):
        if not self.base_table.has_column(self.key_column):
            raise ValueError(
                f"table {self.base_table.name} has no column named {self.key_column.name}"
            )

    def _read_columns(self) -> list[str]:
        return [
            item.name for item in self.base_table.columns if not item.partition_column
        ]

    def _select(self, context: Dict) -> str:
        self_columns: list[str] = self._read_columns()
        return f'select {", ".join(self_columns)}'

    def _from(self, context: Dict):
        return f"from {self.base_table.name}"

    def _cond_to_str(self, cond: Dict, context: Dict[str, str]) -> str:
        in_op_set = {"in", "not in"}

        op: str = cond["op"]
        op = op.strip().lower()
        op = re.sub(r"\s+", " ", op)
        name = cond["name"]
        try:
            value: str = context[name]
        except KeyError as e:
            raise AttributeError(
                f"need to specify a value for {name} in context"
            ) from e

        column = self.base_table.get_column(name)
        if op in in_op_set:
            values = [item.strip() for item in value.split(",")]
        else:
            values = [f"{value}"]

        if not column.is_number_column():
            values = [f"'{item}'" for item in values]

        if op in in_op_set:
            value_str = ", ".join(values)
        else:
            value_str = "".join(values)

        return " ".join([name, op, value_str])

    def _insert_group(self, context: Dict):
        """hive insert overwrite partition information"""
        pass

    def _where_group(self, cond_dicts: List[Dict], context: Dict) -> str:
        """
        Dict has key: name op value
        """
        condition_items = [
            self._cond_to_str(cond_dict, context) for cond_dict in cond_dicts
        ]
        condition_str = " and ".join(condition_items)
        return condition_str

    def _where(self, context: Dict):
        or_conditions = [
            self._where_group(cond_dicts, context).join(["(", ")"])
            for cond_dicts in self.read_filter
        ]
        return " ".join(["where", " or ".join(or_conditions)])

    def _to_table(self):
        pass

    def _sql_set(self, context: Dict):
        pass

    def union(self, **others):
        pass

    def intersection(self, *args):
        return "anc"

    def difference(self):
        pass


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    table1 = Table(
        "ks_ad.orientation_operations",
        "this is a good table",
        columns=[
            Column("id_string", SqlType.string, desc="this is a good column"),
            Column(
                "operation_id",
                SqlType.string,
                desc="this is also a good column",
                partition_column=True,
            ),
        ],
    )

    table2 = Table(
        "second_table",
        "this is a good table",
        columns=[
            Column("user_id", SqlType.string, desc="this is a good column"),
            Column("imeimd5", SqlType.int, desc="this is also a good column"),
            Column(
                "p_date",
                SqlType.float,
                desc="this is also a good column",
                partition_column=True,
            ),
        ],
    )

    user_data_set: SqlSet = SqlSet(
        name="s1",
        desc="a good set",
        base_table=table1,
        key_column=table1.get_column("id_string"),
        read_filter=[[{"op": "=", "name": "operation_id"}]],
        write_filter=[],
    )
    logging.info("%s", user_data_set)

    s2: SqlSet = SqlSet(
        name="s2",
        desc="a good set",
        base_table=table2,
        key_column=table2.get_column("imeimd5"),
        read_filter=[[{}], [{}]],
        write_filter=[],
    )
    logging.info("%s", s2)

    logging.info("%s", table1 == table2)
    logging.info("%s", user_data_set == s2)

    logging.info("%s", user_data_set._select({}))
    logging.info("%s", user_data_set._from({}))
    logging.info("%s", user_data_set._where({"operation_id": "100"}))
