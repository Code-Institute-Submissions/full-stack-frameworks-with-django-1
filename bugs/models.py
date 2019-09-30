from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):
    """
        Creating the Bug Model that creates
        the bug table in the MySQL Database.
    """
    PRIORITIES = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    STATUSES = (
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    tag = models.CharField(max_length=3, default='bug')
    title = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(
                                max_length=8,
                                choices=PRIORITIES,
                                default='LOW')
    screenshot = models.ImageField(
                                    upload_to='bug_screenshots',
                                    blank=True,
                                    null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES, default='IP')
    upvotes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
        Creating the Comment Model
        that creates the comment table
        in the MySQL Database.
    """
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Upvote(models.Model):
    """
        Create the Upvote Model
        that creates the upvote table
        in the MySQL Database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class SavedBug(models.Model):
    """
        Creating the SavedBug Model
        that creates the savedbug table
        in the MySQL Database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
