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
    return render(request, 'basket/basket.html')


@login_required
def add_to_basket_view(request, id):
    """
        View that returns a page
        with all of the contents
        within the basket.
    """
    # quantity = int(request.POST.get('quantity'))
    # basket = request.session.get('basket', {})
    # basket[id] = basket.get(id, quantity)
    # request.session['basket'] = basket
    # return redirect('get-basket')
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if str(id) in basket.keys():
        basket[id] = basket.get(id, int(basket.get(str(id))) + quantity)
    else:
        basket[id] = basket.get(id, quantity)
    request.session['basket'] = basket
    messages.success(request, 'Added item to basket')
    return redirect('get-ticket-detail', id)


@login_required
def amend_basket_view(request, id):
    """
        View that returns a page
        with all of the contents
        within the basket.
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop(id)

    request.session['basket'] = basket
    return redirect('get-basket')
