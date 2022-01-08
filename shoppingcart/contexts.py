from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from plants.models import Plant

def cart_contents(request):
    cart_items = []
    total_price = 0
    plant_count = 0
    cart = request.session.get('cart', {})

    for key, value in cart.items():
        plant = get_object_or_404(Plant, pk=key)
        cart_items.append(plant)
        total_price += plant.price * value
        plant_count += value # or maybe just do a +1?

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'plant_count': plant_count,
    }

    return context
