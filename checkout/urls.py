"""
    Below are the paths for checkouts pages.
    The URL can be further configured from
    the main project urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_checkout_view, name='get-checkout'),
]
