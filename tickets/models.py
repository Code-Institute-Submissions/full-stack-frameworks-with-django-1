from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """
        Creating the Ticket Model that creates
        the ticket table in the MySQL Database.
    """
    TAGS = (
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
    )
    PRIORITIES = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    STATUSES = (
        ('FR', 'Funding Required'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    tag = models.CharField(max_length=7, choices=TAGS, default='BUG')
    title = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.CharField(
                                max_length=8,
                                choices=PRIORITIES,
                                default='LOW',
                                blank=True,
                                null=True)
    screenshot = models.ImageField(
                                    upload_to='ticket_screenshots',
                                    blank=True,
                                    null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUSES, default='IP')
    upvotes = models.IntegerField(default=0)
    upvote_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=19.99)
    earned = models.IntegerField(default=0, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
        # return self.title + ' by ' + self.author


class Comment(models.Model):
    """
        Creating the Comment Model
        that creates the comment table
        in the MySQL Database.
    """
    comment = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
        # return self.comment + ' by ' + self.author


class Upvote(models.Model):
    """
        Create the Upvote Model
        that creates the upvote table
        in the MySQL Database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # user = self.user.username
        # ticket = self.ticket.title
        # return user.capitalize() + ' : ' + ticket


class SavedTicket(models.Model):
    """
        Creating the SavedTicket Model
        that creates the savedticket table
        in the MySQL Database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # user = self.user.username
        # ticket = self.ticket.title
        # return user.capitalize() + ' : ' + ticket
