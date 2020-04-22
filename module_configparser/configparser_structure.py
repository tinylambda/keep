from configparser import ConfigParser


parser = ConfigParser()
parser.read('test.ini')

for section_name in parser.sections():
    print('Section: ', section_name)
    print('Options: ', parser.options(section_name))
    for name, value in parser.items(section_name):
        print('{} = {}'.format(name, value))
    print()

