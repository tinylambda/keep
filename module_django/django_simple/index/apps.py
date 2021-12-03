import time

from django.apps import AppConfig

print('apps.py', time.time())
class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
