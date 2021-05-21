from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
