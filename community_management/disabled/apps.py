from django.apps import AppConfig


class DisabledConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disabled'
