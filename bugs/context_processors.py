from .models import Bug, SavedBug


def total_bug_counter(request):
    """
        Helper Function to get count
        values for base.html pills
    """
    return {
        'bug_count': Bug.objects.filter(status='IP').count(),
    }


def user_submitted_bug_counter(request):
    """
        Helper Function to count
        only the current users submissions
    """
    if request.user.is_authenticated:
        return {
            'user_bug_count': Bug.objects.filter(author=request.user, status='IP').count(),
        }
    else:
        return {
            'user_bug_count': 0,
        }


def user_saved_bug_counter(request):
    """
        Helper Function to count
        only the current users saved
        bugs
    """
    if request.user.is_authenticated:
        return {
            'user_saved_bug_count': SavedBug.objects.filter(user=request.user).count(),
        }
    else:
        return {
            'user_saved_bug_count': 0,
        }
