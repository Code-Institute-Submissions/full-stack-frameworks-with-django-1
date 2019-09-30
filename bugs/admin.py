from django.contrib import admin
from .models import Bug, Comment, Upvote, SavedBug

admin.site.register(Bug)

admin.site.register(Comment)

admin.site.register(Upvote)

admin.site.register(SavedBug)