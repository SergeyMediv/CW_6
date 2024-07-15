from django.db import models
from users.models import User
from config import settings


NULLABLE = {'null': 'True', 'blank': 'True'}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, verbose_name='Ф.И.О')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    comment = models.CharField(max_length=100, verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                              **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('email',)


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                              **NULLABLE)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('theme',)


class Mailing(models.Model):

    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIOD_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус")
    periodicity = models.CharField(
        max_length=150,
        choices=PERIOD_CHOICES,
        default=DAILY,
        verbose_name="Периодичность",
    )
    start_date = models.DateTimeField(
        verbose_name="Дата начала",
        **NULLABLE,
    )
    end_date = models.DateTimeField(verbose_name='Дата окончания', **NULLABLE, help_text='не обязательное поле')
    next_send_time = models.DateTimeField(verbose_name='Время следующей отправки', **NULLABLE)
    clients = models.ManyToManyField(Client, related_name='mailing', verbose_name='Клиенты рассылки')
    message = models.ForeignKey(Message, verbose_name='Cообщение', on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец',  on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.name}, статус: {self.status}"

    def save(self, *args, **kwargs):
        if not self.next_send_time:
            self.next_send_time = self.start_date
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("name",)
        permissions = [
            ('deactivate_mailing', 'Can deactivate mailing'),
            ('view_all_mailings', 'Can view all mailings'),
        ]


class Log(models.Model):

    SUCCESS = 'Успешно'
    FAIL = 'Неуспешно'
    STATUS_CHOICES = [
        (SUCCESS, 'Успешно'),
        (FAIL, 'Неуспешно'),
    ]

    time = models.DateTimeField(
        verbose_name="Дата и время попытки", auto_now_add=True
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Cтатус')
    server_response = models.CharField(
        max_length=150, verbose_name="Ответ сервера почтового сервиса", **NULLABLE
    )
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")

    def __str__(self):
        return f"{self.mailing} {self.time} {self.status} {self.server_response}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
