import argparse


class CustomAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        argparse.Action.__init__(self, *args, **kwargs)
        print('initializing customAction')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print('\t{} = {!r}'.format(name, value))
        print()

    def __call__(self, parser, namespace, values, option_string=None):
        print('Processing customAction for {}'.format(self.dest))
        print('\tparser = {}'.format(id(parser)))
        print('\tvalues = {!r}'.format(values))
        print('\toption_string = {!r}'.format(option_string))

        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        setattr(namespace, self.dest, values)
        print()


parser = argparse.ArgumentParser()
parser.add_argument('-a', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)
results = parser.parse_args(['-a', 'value', '-m', 'multivalue', 'second'])
print(results)

