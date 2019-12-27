from django.test import SimpleTestCase
from tickets.forms import BugForm, FeatureForm, CommentForm, FilterForm


class TestForms(SimpleTestCase):

    def test_bug_form_valid_data(self):
        """
            Test BugForm with valid data.
        """

        form = BugForm(data={
            'title': 'Bug',
            'description': 'Bug Description',
            'priority': 'LOW',
            'status': 'IP'
        })

        self.assertTrue(form.is_valid())

    def test_bug_form_no_data(self):
        """
            Test BugForm with no data.
        """

        form = BugForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_feature_form_valid_data(self):
        """
            Test FeatureForm with valid data.
        """

        form = FeatureForm(data={
            'title': 'Feature',
            'description': 'Feature Description',
            'status': 'FR'
        })

        self.assertTrue(form.is_valid())

    def test_feature_form_no_data(self):
        """
            Test FeatureForm with no data.
        """

        form = FeatureForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_comment_form_valid_data(self):
        """
            Test CommentForm with valid data.
        """

        form = CommentForm(data={
            'comment': 'I am a comment.'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        """
            Test CommentForm with no data.
        """

        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_filter_form_valid_data(self):
        """
            Test FilterForm with valid data.

            There are no required fields,
            so there is no point to
            do a no_data variant test.
        """

        form = FilterForm(data={
            'tag': 'bug',
            'title_or_author': 'Bug',
            'priority': 'low',
            'status': 'ip'
        })

        self.assertTrue(form.is_valid())
