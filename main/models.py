from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class MyUser(AbstractUser):
    activated = models.BooleanField(default=True, db_index=True, verbose_name='Активный?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать сообщение о новых пользователях')

    # def get_absolute_url(self):
    #     return reverse('register_done')
