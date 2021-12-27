from django.apps import AppConfig
from django.dispatch import Signal
from main.utilities import send_activation_notification


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    # label = 'main.apps.MainConfig'


# user_registered = Signal(['instance'])


def user_registered_dispatch(**kwargs):
    send_activation_notification(kwargs['instance'])


# user_registered.connect(user_registered_dispatch)
