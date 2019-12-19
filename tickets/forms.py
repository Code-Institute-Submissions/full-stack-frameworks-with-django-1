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
        Form used to upvote tickets.
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
