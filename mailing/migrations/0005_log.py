# Generated by Django 5.0.3 on 2024-07-09 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailing_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')),
                ('status', models.CharField(choices=[('Успешно', 'Успешно'), ('Неуспешно', 'Неуспешно')], max_length=50, verbose_name='Cтатус')),
                ('server_response', models.CharField(blank='True', max_length=150, null='True', verbose_name='Ответ сервера почтового сервиса')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
