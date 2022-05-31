import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

csv.register_dialect(
    "escaped", escapechar="\\", doublequote=False, quoting=csv.QUOTE_NONE
)
csv.register_dialect("singlequote", quotechar="'", quoting=csv.QUOTE_ALL)

quoting_modes = {getattr(csv, n): n for n in dir(csv) if n.startswith("QUOTE_")}

logging.info("==> %s", quoting_modes)

TEMPLATE = """
Dialect: "{name}"

    delimiter = {dl!r:<6}   sikpinitialspace = {si!r}
    doublequote = {dq!r:<6} quoting = {qu}
    quotechar = {qc!r:<6}   lineterminator = {lt!r}
    escapechar = {ec!r:<6}
"""

for name in sorted(csv.list_dialects()):
    dialect = csv.get_dialect(name)

    logging.info(
        "%s",
        TEMPLATE.format(
            name=name,
            dl=dialect.delimiter,
            si=dialect.skipinitialspace,
            dq=dialect.doublequote,
            qu=quoting_modes[dialect.quoting],
            qc=dialect.quotechar,
            lt=dialect.lineterminator,
            ec=dialect.escapechar,
        ),
    )

    writer = csv.writer(sys.stdout, dialect=dialect)
    writer.writerow(
        (
            "col1",
            1,
            "10/01/2010",
            "special chars: \" ' {} to parse".format(dialect.delimiter),
        )
    )
