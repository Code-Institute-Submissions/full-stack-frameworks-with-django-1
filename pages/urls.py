"""
    Below are the paths for static pages, such as the homepage
    The URL can be further configured from the main project
    urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='main-homepage'),
]
