import argparse


parser = argparse.ArgumentParser(
    description="change the option prefix characters", prefix_chars="-+/"
)
parser.add_argument("-a", action="store_false", default=None, help="turn A off")
parser.add_argument("+a", action="store_true", default=None, help="turn A on")
parser.add_argument("//noarg", "++noarg", action="store_true", default=False)

print(parser.parse_args())


# python argparse_prefix_chars.py -h
# python argparse_prefix_chars.py +a
# python argparse_prefix_chars.py -a
# python argparse_prefix_chars.py //noarg
# python argparse_prefix_chars.py ++noarg
# python argparse_prefix_chars.py --noarg  <--- error
