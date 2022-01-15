from locale import currency
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from checkout.forms import OrderForm
from plants.models import Plant
from .models import Order, OrderLineItem

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            # 'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        # messages.error(request, 'Sorry, your payment cannot be \
        #     processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    cart = request.session.get('cart', {})
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

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

            # Handle the payment via stripe
            order.update_total()
            stripe_total = round(order.total_cost * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY
            )

        # Empty the shoppingcart and redirect back to home
        request.session['cart'] = {}
        return redirect(reverse('home'))
    else:
        order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
        }

        return render(request, 'checkout/checkout.html', context)
