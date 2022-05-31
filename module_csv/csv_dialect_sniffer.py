import csv
import logging
import sys
from io import StringIO

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

csv.register_dialect(
    "escaped", escapechar="\\", doublequote=False, quoting=csv.QUOTE_NONE
)
csv.register_dialect("singlequote", quotechar="'", quoting=csv.QUOTE_ALL)


if __name__ == "__main__":
    samples = []

    for name in sorted(csv.list_dialects()):
        buffer = StringIO()
        dialect = csv.get_dialect(name)
        writer = csv.writer(buffer, dialect=dialect)
        writer.writerow(
            (
                "col1",
                1,
                "10/01/2010",
                "Special chars \" ' {} to parse".format(dialect.delimiter),
            )
        )
        samples.append((name, dialect, buffer.getvalue()))

    sniffer = csv.Sniffer()
    for name, expected, sample in samples:
        logging.info('Dialect: "%s"', name)
        logging.info("In: %s", sample.rstrip())
        dialect = sniffer.sniff(sample, delimiters=",\t")
        reader = csv.reader(StringIO(sample), dialect=dialect)
        logging.info("Parsed:\n %s\n", "\n ".join(repr(r) for r in next(reader)))
