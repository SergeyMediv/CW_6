from django.urls import path
from django.conf.urls.static import static

from config import settings
from mailing.apps import MailingConfig
from mailing.views import (HomeView, ClientListView, ClientUpdateView, ClientCreateView, ClientDeleteView,
                           ClientDetailView)

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('list/', ClientListView.as_view(), name='clients_list'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
