from .models import Bug


def total_bug_counter(request):
    """
        Helper Function to get count
        values for base.html pills
    """
    return {
        'bug_count': Bug.objects.filter(status='IP').count(),
    }


# def user_submitted_bug_counter(request):
#     """
#         Helper Function to count
#         only the current users submissions
#     """
#     return {
#         'user_bug_count': Bug.objects.filter(author_id=request.user, status='IP').count(),
#     }
