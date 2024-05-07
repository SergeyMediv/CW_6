from django.shortcuts import render
from django.views.generic import TemplateView

from mailing.models import Message


class HomeView(TemplateView):
    template_name = 'mailing/base.html'
    extra_context = {
        'title': 'Сервис рассылок'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Message.objects.all()
        return context_data
