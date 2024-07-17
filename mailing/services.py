import smtplib
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.conf import settings

from mailing.models import Mailing, Log


def start_mail():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = Mailing.objects.filter(status__in=[Mailing.STARTED, Mailing.CREATED])

    for mailing in mailings:
        if mailing.end_date and current_datetime >= mailing.end_date:
            mailing.status = Mailing.COMPLETED
            mailing.save()
            continue

        if mailing.next_send_time and current_datetime >= mailing.next_send_time:
            mailing.status = Mailing.STARTED
            try:
                server_response = send_mail(
                    subject=mailing.message.theme,
                    message=mailing.message.text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.clients.all()],
                    fail_silently=False,
                )
                Log.objects.create(status=Log.SUCCESS,
                                   server_response=server_response,
                                   mailing=mailing, )
            except smtplib.SMTPException as e:
                Log.objects.create(status=Log.FAIL,
                                   server_response=str(e),
                                   mailing=mailing, )

            if mailing.periodicity == Mailing.DAILY:
                mailing.next_send_time += timedelta(days=1)
            elif mailing.periodicity == Mailing.WEEKLY:
                mailing.next_send_time += timedelta(weeks=1)
            elif mailing.periodicity == Mailing.MONTHLY:
                mailing.next_send_time += timedelta(days=30)

            mailing.save()


def scheduler_start():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(start_mail, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()
