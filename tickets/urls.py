"""
    Below are the paths for tickets pages, such as
    the ticket detail page. The URL can be
    further configured from the main
    project urls.py file.

    Views can be found inside views.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tickets_view, name='get-tickets'),
    path('<tag>s/', views.get_tickets_tag_view, name='get-tickets-tag'),
    path('<tag>s/submitted/', views.get_user_tickets_view, name='get-user-tickets'),
    path('<tag>s/saved/', views.get_user_saved_tickets_view, name='get-user-saved-tickets'),
    path('bugs/priority/<priority>/', views.get_bugs_priority_view, name='get-bugs-priority'),

    path('<int:pk>/', views.get_ticket_detail_view, name='get-ticket-detail'),

    path('<tag>s/new/', views.add_new_ticket_view, name='add-new-ticket'),
    path('<int:pk>/edit/', views.edit_ticket_view, name='edit-ticket'),
    path('<int:pk>/delete/', views.delete_ticket_view, name='delete-ticket'),

    path('<int:ticket_pk>/new-comment/', views.add_new_comment_view, name='add-new-comment'),
    # edit comment (?maybe?)
    # delete comment (?maybe?)

    path('<int:pk>/upvote-bug/', views.upvote_bug_view, name='upvote-bug'),
    path('<int:pk>/upvote-feature/', views.upvote_feature_view, name='upvote-feature'),

    path('<int:pk>/save/', views.user_save_ticket_view, name='save-ticket'),
    path('<int:pk>/saved/delete/', views.user_delete_saved_ticket_view, name='delete-saved-ticket'),
]
