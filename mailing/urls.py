from django.urls import path
from django.conf.urls.static import static

from config import settings
from mailing.apps import MailingConfig
from mailing.views import HomeView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
