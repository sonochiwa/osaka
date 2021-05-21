from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(extra_context={"section": "sign-in"}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(extra_context={"section": "sign-out"}), name='logout'),
    path('register/', views.register, name='register')
]