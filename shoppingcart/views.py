from django.shortcuts import redirect, render, reverse
from django.shortcuts import get_object_or_404
from plants.models import Plant


def view_cart(request):
    """ Show the cart """

    return render(request, 'shoppingcart/cart.html')


def add_to_cart(request, plant_id):
    """ Add an item to the cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    # If the plant is already in the cart, update the quantity
    if plant_id in list(cart.keys()):
        cart[plant_id] += quantity
    else:
        cart[plant_id] = quantity

    request.session['cart'] = cart

    # return redirect(reverse('all_plants'))
    return render(request, 'shoppingcart/cart.html')
