import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.expressions import Case
from plants.models import Plant
from accounts.models import Users

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(Users, null=True, on_delete=SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    shipping_fee = models.DecimalField(decimal_places=2, max_digits=6)
    order_total = models.DecimalField(decimal_places=2, max_digits=10)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)

    def _generate_order_number(self):
        """ Generate a unique order number """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the total cost everytime a line_item is added
        """

        self.order_total = self.line_items.aggregate(Sum('line_total'))['line_total__sum']
        self.shipping_fee = settings.SHIPPING_FEE
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

    def __str__(self) -> str:
        return f'Plant: {self.plant.common_name} on order: {self.order.order_number}'
