from django import forms
from .models import Bug, Comment, Upvote, SavedBug


class BugForm(forms.ModelForm):
    """
        Form used to submit bugs
        on the front-end
    """
    class Meta:
        model = Bug
        fields = (
                    'title',
                    'description',
                    'priority',
                    'screenshot',
                    'status'
                 )


class CommentForm(forms.ModelForm):
    """
        Form used to submit comments
        on the front-end
    """
    class Meta:
        model = Comment
        fields = ('comment',)


class UpvoteForm(forms.ModelForm):
    """
        Form used to upvote bugs
    """
    class Meta:
        model = Upvote
        fields = ()


class SavedBugForm(forms.ModelForm):
    """
        Form used to save bugs
        on the front-end
    """
    class Meta:
        model = SavedBug
        fields = ()
