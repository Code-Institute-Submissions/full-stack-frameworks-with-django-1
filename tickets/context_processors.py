from .models import Ticket, SavedTicket


def total_ticket_counter(request):
    """
        Helper Function to get count
        values for base.html pills
    """
    return {
        'total_bug_count': Ticket.objects.filter(tag='bug').count(),
        'total_feature_count': Ticket.objects.filter(tag='feature').count(),
    }


def user_submitted_ticket_counter(request):
    """
        Helper Function to count
        only the current users submissions
    """
    if request.user.is_authenticated:
        return {
            'user_submitted_bug_count': Ticket.objects
            .filter(author=request.user, tag='bug')
            .count(),
            'user_submitted_feature_count': Ticket.objects
            .filter(author=request.user, tag='feature')
            .count(),
        }
    else:
        return {
            'user_submitted_bug_count': 0,
            'user_submitted_feature_count': 0,
        }


def user_saved_ticket_counter(request):
    """
        Helper Function to count
        only the current users saved
        tickets
    """
    if request.user.is_authenticated:
        return {
            'user_saved_bug_count': SavedTicket.objects
            .filter(user=request.user, ticket__tag='bug')
            .count(),
            'user_saved_feature_count': SavedTicket.objects
            .filter(user=request.user, ticket__tag='feature')
            .count(),
        }
    else:
        return {
            'user_saved_bug_count': 0,
            'user_saved_feature_count': 0,
        }
