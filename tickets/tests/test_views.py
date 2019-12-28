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

        user = User.objects.create_user(username=username, password=password, is_staff=True)
        author = User.objects.get(username=username)
        login = self.client.login(username=username, password=password)

        self.assertTrue(login)

        self.bug_args = dict(
            tag='BUG',
            title='Test Bug',
            description='Description of a bug...',
            priority='LOW',
            author=author,
            status='IP',
            upvotes=0,
            upvote_price=0,
            earned=0
        )

        self.feature_args = dict(
            tag='FEATURE',
            title='Test Feature',
            description='Description of a feature...',
            priority='',
            author=author,
            status='FR',
            upvotes=0,
            upvote_price=19.99,
            earned=0
        )

        self.bug = Ticket.objects.create(**self.bug_args)
        self.feature = Ticket.objects.create(**self.feature_args)

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

    def test_edit_ticket_POST(self):
        """
            Test that a ticket can be updated
            via a POST request.
        """
        
        self.bug_args.update({'title': 'Test Bug UPDATED'})

        response = self.client.post(reverse('edit-ticket', args=[self.bug.pk]), self.bug_args)

        ticket = Ticket.objects.get(pk=self.bug.pk)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ticket.title, 'Test Bug UPDATED')

    def test_delete_ticket_POST(self):
        """
            Test that a ticket can be deleted
            via a POST request.
        """

        delete_me = Ticket.objects.create(
            title='Delete me',
            description='I want to be deleted.',
            author=self.bug_args.get('author'),
            status='IP',
        )


        query = Ticket.objects.filter(title='Delete me')
        self.assertEquals(query.count(), 1)

        ticket = Ticket.objects.get(title='Delete me')
        response = self.client.post(reverse('delete-ticket', args=[ticket.pk]))

        self.assertEquals(response.status_code, 302)
        query = Ticket.objects.filter(title='Delete me')
        self.assertEquals(query.count(), 0)
