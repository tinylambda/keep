from configparser import ConfigParser
import codecs


parser = ConfigParser()
parser.read('test3.ini', encoding='utf-8')

password = parser.get('bug_tracker', 'password')

# The value returned by get() is a Unicode string,
# so in order to print it safely it must be re-encoded as UTF-8.
print('Password: ', password.encode('utf-8'))
print('Type: ', type(password))
print('repr(): ', repr(password))


