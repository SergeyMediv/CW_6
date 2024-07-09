from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': 'True', 'blank': 'True'}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=35, verbose_name='Email', unique=True)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE, help_text='Номер телефона')
    token = models.CharField(max_length=35, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
