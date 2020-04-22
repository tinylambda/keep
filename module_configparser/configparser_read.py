from configparser import ConfigParser


parser = ConfigParser()
parser.read('test.ini')

print(parser.get('bug_tracker', 'url'))

