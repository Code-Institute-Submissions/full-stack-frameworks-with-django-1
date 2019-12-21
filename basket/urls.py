"""
    Below are the paths for basket pages. 
    The URL can be further configured
    from the main project urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_basket_view, name='get-basket'),
    path('add/<int:id>/', views.add_to_basket_view, name='add-to-basket'),
    path('amend/<int:id>/', views.amend_basket_view, name='amend-basket'),
]
