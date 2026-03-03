from django.apps import AppConfig


class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'

class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        import firstapp.signals