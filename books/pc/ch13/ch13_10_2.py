import sys
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read('config.ini')
print(cfg.sections())

print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.getint('server', 'nworkers'))
print(cfg.get('server', 'signature'))

cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
cfg.write(sys.stdout)
