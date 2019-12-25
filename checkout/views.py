from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import OrderItem
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket
import stripe


stripe.api_key = settings.STRIPE_SECRET

@login_required
def get_checkout_view(request):
    """
        View that returns the checkout
        page and allows the user to
        pay for feature upvotes.
    """
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.order_date = timezone.now()
            order.save()

            basket = request.session.get('basket', {})
            total = 0

            for id, quantity in basket.items():
                ticket = get_object_or_404(Ticket, pk=id)
                total += quantity * ticket.upvote_price
                order_item = OrderItem(order=order, ticket=ticket, quantity=quantity)
                order_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Error! Your card was declined.')

            if customer.paid:
                for id, quantity in basket.items():
                    ticket = Ticket.objects.get(pk=id)
                    ticket.upvotes += quantity
                    ticket.earned += quantity * ticket.upvote_price
                    if ticket.status == 'FR' and ticket.status is not 'C':
                        ticket.status = 'IP'
                    ticket.save()
                messages.success(request, 'Success! You have paid.')
                request.session['basket'] = {}
                return redirect('main-homepage')
            else:
                messages.error(request, 'Error! We were unable to take payment.')
        else:
            print(payment_form.errors)
            messages.error(request, 'Error! We were unable to take payment.')
        return render(request, 'checkout/checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    else:
        basket = request.session.get('basket', {})
        if basket:
            payment_form = PaymentForm()
            order_form = OrderForm()
            return render(request, 'checkout/checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
        else:
            messages.error(request, 'Error! You have nothing to checkout.')
            return redirect('main-homepage')