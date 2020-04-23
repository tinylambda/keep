import configparser


parser = configparser.ConfigParser()
parser.read('test6.ini')

print(parser.get('example', 'message'))
