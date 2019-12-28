from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tickets.views import get_tickets_view, get_tickets_tag_view, \
    get_user_tickets_view, get_user_saved_tickets_view, \
    get_bugs_priority_view, get_ticket_detail_view, \
    add_new_ticket_view, edit_ticket_view, delete_ticket_view, \
    add_new_comment_view, edit_comment_view, delete_comment_view, \
    upvote_bug_view, user_save_ticket_view, \
    user_delete_saved_ticket_view, filter_tickets_view


class TestUrls(SimpleTestCase):

    def test_get_tickets_resolves(self):
        """
            Test that URL is set up correctly
            for get_tickets_view.
        """

        url = reverse('get-tickets')
        self.assertEquals(resolve(url).func, get_tickets_view)

    def test_get_tickets_tag_resolves(self):
        """
            Test that URL is set up correctly
            for get_tickets_tag_view passing
            the tag of 'bug'.
        """

        url = reverse('get-tickets-tag', args=['bug'])
        self.assertEquals(resolve(url).func, get_tickets_tag_view)

    def test_get_user_tickets_resolves(self):
        """
            Test that URL is set up correctly
            for get_user_tickets_view passing
            the tag of 'feature'.
        """

        url = reverse('get-user-tickets', args=['feature'])
        self.assertEquals(resolve(url).func, get_user_tickets_view)

    def test_get_user_saved_tickets_resolves(self):
        """
            Test that URL is set up correctly
            for get_user_saved_tickets_view
            passing the tag of 'bug'.
        """

        url = reverse('get-user-saved-tickets', args=['bug'])
        self.assertEquals(resolve(url).func,
                          get_user_saved_tickets_view)

    def test_get_bug_priority_resolves(self):
        """
            Test that URL is set up correctly
            for get_bugs_priority_view passing
            the priority of 'critical'.
        """

        url = reverse('get-bugs-priority', args=['critical'])
        self.assertEquals(resolve(url).func, get_bugs_priority_view)

    def test_get_ticket_detail_resolves(self):
        """
            Test that URL is set up correctly
            for get_ticket_detail_view passing
            the pk of 1.
        """

        url = reverse('get-ticket-detail', args=[1])
        self.assertEquals(resolve(url).func, get_ticket_detail_view)

    def test_get_ticket_detail_resolves(self):
        """
            Test that URL is set up correctly
            for add_new_ticket_view passing
            the tag of 'feature'.
        """

        url = reverse('add-new-ticket', args=['feature'])
        self.assertEquals(resolve(url).func, add_new_ticket_view)

    def test_edit_ticket_resolves(self):
        """
            Test that URL is set up correctly
            for edit_ticket_view passing
            the pk of 1.
        """

        url = reverse('edit-ticket', args=[1])
        self.assertEquals(resolve(url).func, edit_ticket_view)

    def test_delete_ticket_resolves(self):
        """
            Test that URL is set up correctly
            for delete_ticket_view passing
            the pk of 1.
        """

        url = reverse('delete-ticket', args=[1])
        self.assertEquals(resolve(url).func, delete_ticket_view)

    def test_add_new_comment_resolves(self):
        """
            Test that URL is set up correctly
            for add_new_comment_view passing
            the ticket_pk of 1.
        """

        url = reverse('add-new-comment', args=[1])
        self.assertEquals(resolve(url).func, add_new_comment_view)

    def test_edit_comment_resolves(self):
        """
            Test that URL is set up correctly
            for edit_comment_view passing
            the ticket_pk of 1 and
            comment_pk of 1
        """

        url = reverse('edit-comment', args=[1, 1])
        self.assertEquals(resolve(url).func, edit_comment_view)

    def test_edit_comment_resolves(self):
        """
            Test that URL is set up correctly
            for delete_comment_view passing
            the ticket_pk of 1 and
            comment_pk of 1
        """

        url = reverse('delete-comment', args=[1, 1])
        self.assertEquals(resolve(url).func, delete_comment_view)

    def test_upvote_bug_resolves(self):
        """
            Test that URL is set up correctly
            for upvote_bug_view passing
            the pk of 1.
        """

        url = reverse('upvote-bug', args=[1])
        self.assertEquals(resolve(url).func, upvote_bug_view)

    def test_save_ticket_resolves(self):
        """
            Test that URL is set up correctly
            for user_save_ticket_view passing
            the pk of 1.
        """

        url = reverse('save-ticket', args=[1])
        self.assertEquals(resolve(url).func, user_save_ticket_view)

    def test_delete_saved_ticket_resolves(self):
        """
            Test that URL is set up correctly
            for user_delete_saved_ticket_view
            passing the pk of 1.
        """

        url = reverse('delete-saved-ticket', args=[1])
        self.assertEquals(resolve(url).func,
                          user_delete_saved_ticket_view)

    def test_filter_tickets_resolves(self):
        """
            Test that URL is set up correctly
            for filter_tickets_view.
        """

        url = reverse('filter-tickets')
        self.assertEquals(resolve(url).func, filter_tickets_view)
