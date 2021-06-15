from django.urls import path
from . import views


app_name = 'feedback'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]