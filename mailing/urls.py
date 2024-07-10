from django.urls import path
from django.conf.urls.static import static

from config import settings
from mailing.apps import MailingConfig
from mailing.views import (HomeView, ClientListView, ClientUpdateView, ClientCreateView, ClientDeleteView,
                           ClientDetailView, MessageListView, MessageUpdateView, MessageCreateView, MessageDeleteView,
                           MessageDetailView, MailingListView, MailingUpdateView, MailingCreateView, MailingDeleteView,
                           MailingDetailView, LogListView)

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('list/', ClientListView.as_view(), name='client_list'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message_view/<int:pk>', MessageDetailView.as_view(), name='message_view'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing_view/<int:pk>', MailingDetailView.as_view(), name='mailing_view'),
    path('log_list/', LogListView.as_view(), name='log_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
