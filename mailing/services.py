from django.core.mail import send_mail
from django.conf import settings


def send():
    perem = send_mail(subject='hello', message='123', from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['mirkulok@yandex.ru'])
    print('hello')
