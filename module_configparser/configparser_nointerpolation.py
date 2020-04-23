from configparser import ConfigParser


parser = ConfigParser(interpolation=None)
parser.read('test11.ini')

print('Without interpolation: ', parser.get('bug_tracker', 'url'))

