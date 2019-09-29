"""
    Below are the paths for users pages, such as the
    registration page. The URL can be further
    configured from the main project
    urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='user-registration'),
    path('user-profile/', views.profile_view, name='user-profile'),
    # django.contrib.auth
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
]
