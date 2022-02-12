from django.shortcuts import get_object_or_404
from plants.models import Plant
from checkout.models import Order


def cart_contents(request):
    cart_items = []
    cart = request.session.get('cart', {})
    total_price = 0

    # Add to the cart
    for key, value in cart.items():
        plant = get_object_or_404(Plant, pk=key)
        cart_items.append({
            'id': plant.id,
            'common_name': plant.common_name,
            'price': plant.price,
            'amount': value,
            'image_url': plant.image_url,
            'stock': plant.stock,
        })
        total_price += value * round(plant.price * 100)

    order = Order()
    total_price += round(order.shipping_fee * 100)
    context = {
        'cart_items': cart_items,
        'plant_count': len(cart_items),
        'total_price': total_price,
    }

    return context
