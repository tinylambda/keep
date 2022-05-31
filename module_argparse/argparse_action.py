import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", action="store", dest="simple_value", help="store a simple value"
)
parser.add_argument(
    "-c",
    action="store_const",
    const="value-to-store",
    dest="constant_value",
    help="store a const value",
)
parser.add_argument(
    "-t",
    action="store_true",
    default=False,
    dest="boolean_t",
    help="set a switch to true",
)
parser.add_argument(
    "-f",
    action="store_false",
    default=True,
    dest="boolean_f",
    help="set a switch to false",
)
parser.add_argument(
    "-a",
    action="append",
    default=[],
    dest="collection",
    help="add repeated values to a list",
)
parser.add_argument(
    "-A",
    action="append_const",
    dest="const_collection",
    const="value-1-to-append",
    default=[],
    help="add different values to list",
)
parser.add_argument(
    "-B",
    action="append_const",
    dest="const_collection",
    const="value-2-to-append",
    help="add different values to list",
)
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

results = parser.parse_args()
print(f"simple value = {results.simple_value!r}")
print(f"const_value = {results.constant_value!r}")
print(f"boolean_t = {results.boolean_t!r}")
print(f"boolean_f = {results.boolean_f!r}")
print(f"collection = {results.collection!r}")
print(f"const_collection = {results.const_collection!r}")

# python argparse_action.py -h
# python argparse_action.py -s value
# python argparse_action.py -c
# python argparse_action.py -t
# python argparse_action.py -f
# python argparse_action.py -a one -a two -a three
# python argparse_action.py -B -A
