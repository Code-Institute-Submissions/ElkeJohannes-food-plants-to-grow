from django.shortcuts import render, redirect, reverse
from checkout.forms import OrderForm
from plants.models import Plant
from .models import Order, OrderLineItem


def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect(reverse('all_plants'))

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            # Save the form. If user is logged in, add the user to the order.
            order = order_form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

        # Create a line item in the order for every plant
        for item_id, item_data in cart.items():
            plant = Plant.objects.get(id=item_id)
            if isinstance(item_data, int):
                order_line_item = OrderLineItem(
                    order=order,
                    plant=plant,
                    quantity=item_data,
                )
                order_line_item.save()
        # Empty the shopping and redirect back to home
        request.session['cart'] = {}
        return redirect(reverse('home'))
    else:
        order_form = OrderForm()
    
        context = {
            'order_form': order_form,
        }

        return render(request, 'checkout/checkout.html', context)
