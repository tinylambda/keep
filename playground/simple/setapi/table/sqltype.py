import enum

SQL_TYPE_DELIMITER = "."


class SqlType(enum.Enum):
    int = {
        "is_number": True,
        "is_float": False,
    }

    bigint = {
        "is_number": True,
        "is_float": False,
    }

    smallint = {
        "is_number": True,
        "is_float": False,
    }

    long = {
        "is_number": True,
        "is_float": False,
    }

    float = {
        "is_number": True,
        "is_float": True,
    }

    double = {
        "is_number": True,
        "is_float": True,
    }

    string = {
        "is_number": False,
    }

    def __init__(self, vals):
        self.is_number = vals["is_number"]
        self.is_float = vals.get("is_float", False)
        self.sub_type = None

    @classmethod
    def value_of(cls, type_string: str):
        if not isinstance(type_string, str):
            raise ValueError(
                f"type_string should be a string argument but got {type_string}"
            )
        else:
            type_string = type_string.strip()
            if len(type_string) == 0:
                raise ValueError(f"type_string is empty {type_string}")

        h, *tail = type_string.split(SQL_TYPE_DELIMITER, maxsplit=1)
        try:
            sql_type = SqlType[h]
        except KeyError as e:
            raise ValueError(f"{h} is not a valid sql type") from e


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    type_str = "string.json"
    my_type: SqlType = SqlType.value_of(type_str)
    logging.info("%s", my_type)

    type_str = "xxx.json"
    my_type: SqlType = SqlType.value_of(type_str)
    logging.info("%s", my_type)
