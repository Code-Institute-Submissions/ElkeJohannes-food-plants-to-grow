from django.shortcuts import render


def view_cart(request):
    """ Show the cart """

    return render(request, 'shoppingcart/cart.html')
