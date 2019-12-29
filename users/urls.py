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
    path('user-profile/change-email/', views.change_email_view,
         name='user-change-email'),
    path('user-profile/change-password/', views.change_password_view,
         name='user-change-password'),
    # django.contrib.auth
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True
        ), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'
        ), name='user-logout'),
]
