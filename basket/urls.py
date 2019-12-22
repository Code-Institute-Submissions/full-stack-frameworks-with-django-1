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
    path('<int:id>/add/', views.add_to_basket_view, name='add-to-basket'),
    path('<int:id>/amend/', views.amend_basket_view, name='amend-basket'),
    path('<int:id>/delete/', views.delete_basket_item_view, name='delete-basket-item'),
]
