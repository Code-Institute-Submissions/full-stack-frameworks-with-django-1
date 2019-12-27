from django.test import TestCase
from django.contrib.auth.models import User
from tickets.models import Ticket, Comment, Upvoted, SavedTicket


class TestModels(TestCase):

    def setUp(self):
        """
            Set up some test data.
        """

        user = User.objects.create_user(username=username, password=password)
        author = User.objects.get(username=username)

        self.bug = Ticket.object.create(
            tag='BUG',
            title='Test Bug',
            author=author,
            upvote_price=0
        )