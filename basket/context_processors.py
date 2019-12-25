from django.shortcuts import get_object_or_404
from tickets.models import Ticket


def basket_contents(request):
    """
        Set up the basket and ensure
        basket content is available
        on every page.
    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    upvote_count = 0
    for id, quantity in basket.items():
        ticket = get_object_or_404(Ticket, pk=id)
        total += quantity * ticket.upvote_price
        upvote_count += quantity
        basket_items.append({'id': id, 'quantity': quantity, 'ticket': ticket})
    return {'basket_items': basket_items, 'total': total, 'upvote_count': upvote_count}
