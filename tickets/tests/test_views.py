from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from tickets.models import Ticket, Comment, Upvote, SavedTicket
from decimal import Decimal
import json


class TestViews(TestCase):

    def setUp(self):
        """
            Set up logged in user
            and create a ticket
            to test.
        """

        username = 'testAppUser'
        password = 'testAppPass'

        user = User.objects.create_user(username=username, password=password)
        author = User.objects.get(username=username)
        login = self.client.login(username=username, password=password)

        self.assertTrue(login)

        self.bug = Ticket.objects.create(
            tag='BUG',
            title='Test Bug',
            author=author,
            upvote_price=0
        )

        self.feature = Ticket.objects.create(
            tag='FEATURE',
            title='Test Feature',
            author=author
        )

    def test_get_tickets_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-tickets'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/get-tickets.html')

    def test_get_tickets_tag_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-tickets-tag', args=['bug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/get-tickets.html')

    def test_get_tickets_tag_404(self):
        """
            Test that if the tag doesn't
            exist, it should 404.
        """

        response = self.client.get(reverse('get-tickets-tag', args=['random']))
        self.assertEquals(response.status_code, 404)

    def test_get_bugs_priority_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-bugs-priority', args=['critical']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/get-bugs.html')

    def test_get_bugs_priority_404(self):
        """
            Test that if the priority
            doesn't exist, it should 404.
        """

        response = self.client.get(reverse('get-bugs-priority', args=['random']))
        self.assertEquals(response.status_code, 404)

    def test_get_user_tickets_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-user-tickets', args=['bug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/get-user-tickets.html')

    def test_get_user_saved_tickets_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-user-saved-tickets', args=['bug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/get-user-saved-tickets.html')

    def test_get_ticket_detail_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('get-ticket-detail', args=[self.bug.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/ticket-detail.html')

    def test_add_new_ticket_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('add-new-ticket', args=['bug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/ticket-form.html')

    def test_add_new_ticket_POST_add_bug(self):
        """
            Test that a new bug can be
            added via POST request
        """

        response = self.client.post(reverse('add-new-ticket', args=['bug']), {
            'title': 'This is a bug',
            'description': 'Description',
            'priority': 'HIGH',
            'status': 'IP',
            'upvote_price': 0
        })

        ticket = Ticket.objects.get(title='This is a bug')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ticket.title, 'This is a bug')

    def test_add_new_ticket_POST_add_feature(self):
        """
            Test that a new feature can be
            added via POST request
        """

        response = self.client.post(reverse('add-new-ticket', args=['feature']), {
            'title': 'This is a feature',
            'description': 'Description',
            'status': 'FR',
        })

        ticket = Ticket.objects.get(title='This is a feature')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ticket.title, 'This is a feature')
        self.assertEquals(ticket.upvote_price, Decimal('19.99'))

    def test_edit_ticket_GET(self):
        """
            Test that the status code and
            template used are correct.
        """

        response = self.client.get(reverse('edit-ticket', args=[self.bug.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tickets/ticket-form.html')
