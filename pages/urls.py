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
    path('terms-and-conditions/', views.terms_and_conditions_view,
         name='main-t-and-c'),
    path('refund-policy/', views.refund_policy_view, name='main-refund'),
    path('privacy-policy/', views.privacy_policy_view, name='main-privacy'),
]
