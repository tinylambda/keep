import time

from django.apps import AppConfig

print(__file__, time.time())


class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'

    def ready(self):
        print(self, 'ready', time.time())
