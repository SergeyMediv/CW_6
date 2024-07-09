from django.contrib import admin

from mailing.models import Client, Message, Mailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)
    search_fields = ('email', 'name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ('theme',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
