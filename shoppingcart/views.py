from django.shortcuts import redirect, render, reverse
from django.shortcuts import get_object_or_404
from plants.models import Plant


def view_cart(request):
    """ Show the cart """
    
    return render(request, 'shoppingcart/view_cart.html')


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

    return render(request, 'shoppingcart/view_cart.html')


def update_cart(request):
    """ Update the number of items in the cart """
    
    cart = request.session.get('cart', {})
    for plant_id, quantity in cart.items():
        quantity = int(request.POST.get('quantity_' + str(plant_id)))
        cart[plant_id] = quantity

    request.session['cart'] = cart

    return redirect(reverse('checkout'))


def delete_from_cart(request, plant_id):
    """ Remove an item from the shoppingcart """

    cart = request.session.get('cart', {})
    cart.pop(plant_id)
    request.session['cart'] = cart

    return render(request, 'shoppingcart/view_cart.html')
