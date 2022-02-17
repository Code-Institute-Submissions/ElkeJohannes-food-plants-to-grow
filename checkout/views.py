from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from checkout.forms import OrderForm
from plants.models import Plant
from accounts.models import UserAccount
from accounts.forms import UserAccountForm
from .models import OrderLineItem
from shoppingcart.contexts import cart_contents
from django.contrib import messages

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(content=e, status=400)


def checkout(request):
    cart = request.session.get('cart', {})
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            # Save the form. If user is logged in, add the user to the order.
            order = order_form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
                # If user checked the box to save
                # save the info to the profile
                if request.session.get('save_info'):
                    current_user = request.user
                    user_profile = UserAccount.objects.get(pk=current_user.id)
                    user_account_form = UserAccountForm(request.POST,
                                                        instance=user_profile)
                    user_account_form.save()
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
            order.update_total()

        # Empty the shoppingcart and redirect back to home
        request.session['cart'] = {}
        messages.success(request, 'Order succesfull! Congratulations!')
        messages.success(request, 'You can find a confirmation in your email inbox')
        return redirect(reverse('home'))
    else:
        # Prepare stripe payment intent
        current_cart = cart_contents(request)
        stripe_total = current_cart['total_price']
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        if request.user.is_authenticated:
            current_user = request.user
            user_profile = UserAccount.objects.get(pk=current_user.id)
            order_form = OrderForm(instance=user_profile)
        else:
            order_form = OrderForm()
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)
