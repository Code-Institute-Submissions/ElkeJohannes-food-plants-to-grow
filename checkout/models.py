import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import Case
from plants.models import Plant
from accounts.models import Account
from django_countries.fields import CountryField

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(Account, null=True, on_delete=SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=80, null=False, blank=False)
    shipping_street_name = models.CharField(max_length=80, null=False, blank=False)
    shipping_street_number = models.CharField(max_length=80, null=False, blank=False)
    shipping_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    shipping_county = models.CharField(max_length=80, null=True, blank=True)
    shipping_postcode = models.CharField(max_length=20, null=True, blank=True)
    shipping_country = CountryField(blank_label='Country', null=False, blank=False)
    billing_street_name = models.CharField(max_length=80, null=False, blank=False)
    billing_street_number = models.CharField(max_length=80, null=False, blank=False)
    billing_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    billing_country = CountryField(blank_label='Country', null=False, blank=False)
    shipping_fee = models.DecimalField(decimal_places=2, max_digits=6, default=00.00)
    order_total = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10, default=00.00)

    def _generate_order_number(self):
        """ Generate a unique order number """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the total cost everytime a line_item is added
        """

        self.order_total = self.line_items.aggregate(Sum('line_total'))['line_total__sum']
        if self.order_total == None:
            self.order_total = Decimal(00.00)
        self.shipping_fee = Decimal(15.75)
        self.total_cost = self.order_total + self.shipping_fee
        
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=CASCADE, related_name='line_items')
    plant = models.ForeignKey(Plant, null=True, blank=False, on_delete=CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.line_total = self.plant.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Plant: {self.plant.common_name} on order: {self.order.order_number}'
