from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def get_basket_view(request):
    """
        View that returns a page
        with all of the contents
        within the basket.
    """
    meta = {
        'title': 'Basket',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'basket/basket.html', context)


@login_required
def add_to_basket_view(request, id):
    """
        View that allows the user
        to add a feature to basket.
    """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        basket = request.session.get('basket', {})
        if str(id) in basket.keys():
            basket[id] = basket.get(id, int(basket.get(str(id))) + quantity)
        else:
            basket[id] = basket.get(id, quantity)
        request.session['basket'] = basket
        messages.success(request,
                         'Success! Feature has been added to your basket.')
        return redirect('get-basket')
    else:
        messages.error(request,
                       'Error! You can\'t go to this URL directly.')
        return redirect('get-ticket-detail', id)


@login_required
def amend_basket_view(request, id):
    """
        View that allows the user
        to amend their basket.
    """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        basket = request.session.get('basket', {})

        if quantity > 0:
            basket[id] = quantity
        else:
            basket.pop(str(id))

        request.session['basket'] = basket
        messages.success(request,
                         'Success! Feature has been updated in your basket.')
    else:
        messages.error(request,
                       'Error! You can\'t go to this URL directly.')
    return redirect('get-basket')


@login_required
def delete_basket_item_view(request, id):
    """
        View that allows the user
        to remove an item from their
        basket.
    """
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        basket.pop(str(id))
        request.session['basket'] = basket
        messages.success(request,
                         'Success! Feature has been removed from your basket.')
    else:
        messages.error(request,
                       'Error! You can\'t go to this URL directly.')
    return redirect('get-basket')
