from configparser import ConfigParser
import os


filename = 'test10.ini'
config = ConfigParser()
config.read([filename])

value = config.get('escape', 'value')
print(value)

