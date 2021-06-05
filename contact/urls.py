from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact')
]
