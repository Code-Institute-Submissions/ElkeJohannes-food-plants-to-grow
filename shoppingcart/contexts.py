from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from plants.models import Plant

def cart_contents(request):

    cart_items = []
    total_price = 0
    plant_count = 0
    cart = request.session.get('cart', {})

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'plant_count': plant_count,
    }

    return context
