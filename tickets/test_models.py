from django.test import TestCase
from django.contrib.auth.models import User
from tickets.models import Ticket
from decimal import Decimal


class TestModels(TestCase):

    def setUp(self):
        """
            Set up some test data.
        """

        username = 'testAppUser'
        password = 'testAppPass'

        user = User.objects.create_user(username=username, password=password)
        author = User.objects.get(username=username)

        self.bug = Ticket.objects.create(
            title='Test Bug',
            description='Description of bug',
            author=author
        )

    def test_ticket_required_not_empty(self):
        """
            Test Ticket required values
            are not empty.
        """

        self.assertTrue(self.bug.title != '')
        self.assertTrue(self.bug.description != '')
        self.assertTrue(self.bug.author != '')

    def test_ticket_defaults_work(self):
        """
            Test Ticket defaults are working
            as intended.
        """

        self.assertEquals(self.bug.tag, 'BUG')
        self.assertEquals(self.bug.priority, 'LOW')
        self.assertEquals(self.bug.status, 'IP')
        self.assertEquals(self.bug.upvotes, 0)
        self.assertEquals(self.bug.upvote_price, 19.99)
        self.assertEquals(self.bug.earned, 0)

    def test_ticket_can_be_overriden(self):
        """
            Test that the ticket defaults
            can be overriden.
        """

        self.bug.tag = 'FEATURE'
        self.bug.priority = None
        self.bug.status = 'FR'
        self.bug.upvotes += 1
        self.bug.upvote_price = 29.99
        self.bug.earned = 29.99

        self.assertEquals(self.bug.tag, 'FEATURE')
        self.assertEquals(self.bug.priority, None)
        self.assertEquals(self.bug.status, 'FR')
        self.assertEquals(self.bug.upvotes, 1)
        self.assertEquals(self.bug.upvote_price, 29.99)
        self.assertEquals(self.bug.earned, 29.99)
