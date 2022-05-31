import logging
import sys

import sqlparse

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == "__main__":
    sql = "select * from a;select * from b"
    logging.info("%s", sqlparse.split(sql))

    sql = 'select col1, "\;go\;" from a;select col2 from b;insert overwrite table result_table partition(a="100") select  col1 from tableC'
    logging.info("%s", sqlparse.split(sql))
