from django.conf import settings
from django.shortcuts import get_object_or_404
from plants.models import Plant

def cart_contents(request):
    cart_items = []
    total_price = 0
    plant_count = 0
    cart = request.session.get('cart', {})

    # Add to the cart
    for key, value in cart.items():
        plant = get_object_or_404(Plant, pk=key)
        cart_items.append({
            'id': plant.id,
            'common_name': plant.common_name,
            'price': plant.price,
            'amount': value,
            'image': plant.image_url,
            'stock': plant.stock,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'plant_count': len(cart_items),
    }

    return context
