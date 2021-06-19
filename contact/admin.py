from django.contrib import admin
from .models import Contact, Mailing
from django.utils.html import format_html
from django.urls import path
from .views import mailing

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'mailing')

    def mailing(self, obj):
        return format_html('<a class="button" href="contact/mailing/{}/">Отправить</a>'.format(obj.id))

    mailing.short_description = 'Рассылка'
    mailing.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('contact/mailing/<int:id>/', self.admin_site.admin_view(mailing)),
        ] 
        return custom + urls
