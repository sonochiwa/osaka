from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')