"""
    Below are the paths for users pages, such as the
    registration page. The URL can be further
    configured from the main project
    urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='user-registration'),
]
