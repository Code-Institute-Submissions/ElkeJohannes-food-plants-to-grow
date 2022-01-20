"""
Code below mostly comes from the Code Institute 'Boutique Ado' Project
"""

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from plants.models import Plant

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    shipping_country__iexact=shipping_details.address.country,
                    shipping_postcode__iexact=shipping_details.address.postal_code,
                    shipping_town_or_city__iexact=shipping_details.address.city,
                    shipping_street_name__iexact=shipping_details.address.line1,
                    shipping_street_number__iexact=shipping_details.address.line2,
                    shipping_county__iexact=shipping_details.address.state,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    shipping_country=shipping_details.address.country,
                    shipping_postcode=shipping_details.address.postal_code,
                    shipping_town_or_city=shipping_details.address.city,
                    shipping_street_name=shipping_details.address.line1,
                    shipping_street_number=shipping_details.address.line2,
                    shipping_county=shipping_details.address.state,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    plant = Plant.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        plant=plant,
                        quantity=item_data,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
