from django import forms
from .models import Ticket, Comment, Upvote, SavedTicket


class BugForm(forms.ModelForm):
    """
        Form used to submit tickets
        with the tag of bug on
        the front-end.
    """
    class Meta:
        model = Ticket
        fields = (
                    'title',
                    'description',
                    'priority',
                    'screenshot',
                    'status'
                 )


class FeatureForm(forms.ModelForm):
    """
        Form used to submit tickets
        with the tag of feature on
        the front-end.
    """
    class Meta:
        model = Ticket
        fields = (
                    'title',
                    'description',
                    'status'
                 )


class CommentForm(forms.ModelForm):
    """
        Form used to submit comments
        on the front-end.
    """
    class Meta:
        model = Comment
        fields = ('comment',)


class UpvoteForm(forms.ModelForm):
    """
        Form used to upvote tickets
        (bugs only) on the front-end.
    """
    class Meta:
        model = Upvote
        fields = ()


class SavedTicketForm(forms.ModelForm):
    """
        Form used to save tickets
        on the front-end.
    """
    class Meta:
        model = SavedTicket
        fields = ()


class FilterForm(forms.Form):
    """
        Form used to filter tickets
        on the front-end.
    """
    TAGS = (
        ('', '---------'),
        ('bug', 'Bug'),
        ('feature', 'Feature'),
    )
    PRIORITIES = (
        ('', '---------'),
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    STATUSES = (
        ('', '---------'),
        ('fr', 'Funding Required'),
        ('ip', 'In Progress'),
        ('c', 'Completed'),
    )
    tag = forms.ChoiceField(label='Type', choices=TAGS, required=False)
    title_or_author = forms.CharField(label='Title of the ticket or the authors name', required=False)
    priority = forms.ChoiceField(label='Priority', choices=PRIORITIES, required=False)
    status = forms.ChoiceField(label='Status', choices=STATUSES, required=False)
