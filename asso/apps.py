from django.apps import AppConfig


class AssoConfig(AppConfig):
    name = 'asso'

    def ready(self):
        import asso.signals