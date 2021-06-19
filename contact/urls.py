from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subscription, name='contact'),
    path('mailing/<int:id>', views.mailing, name='mailing'),
]
