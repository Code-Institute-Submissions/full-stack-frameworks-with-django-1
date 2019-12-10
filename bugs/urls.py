"""
    Below are the paths for bugs pages, such as the
    bug detail page. The URL can be further
    configured from the main project
    urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bugs_view, name='get-bugs'),
    path('submitted-bugs/', views.get_user_bugs_view, name='get-user-bugs'),
    path('priority/critical/', views.get_bugs_view, name='get-critical-bugs'),
    path('priority/high/', views.get_bugs_view, name='get-high-bugs'),
    path('priority/medium/', views.get_bugs_view, name='get-medium-bugs'),
    path('priority/low/', views.get_bugs_view, name='get-low-bugs'),
    path('<int:pk>/', views.bug_detail_view, name='bug-detail'),
    path('new/', views.create_bug_view, name='new-bug'),
    path('<int:pk>/edit/', views.edit_bug_view, name='edit-bug'),
    path('<int:pk>/delete/', views.delete_bug_view, name='delete-bug'),
    path('comment/<bug_pk>/new/', views.create_or_edit_comment_view, name='new-comment'),
    path('<int:pk>/upvote/', views.upvote_bug_view, name='upvote-bug'),
    path('<int:pk>/saved/', views.user_save_bug_view, name='save-bug'),
    path('<int:pk>/saved/delete', views.delete_saved_bug_view, name='delete-saved-bug'),
    path('saved-bugs/', views.get_user_saved_bugs_view, name='get-saved-bugs'),
]
