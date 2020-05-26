from django.apps import AppConfig


class HosmngConfigdjango_mysql(AppConfig):
    name = 'hosmng'

    def ready(self):
     	import hosmng.signals
