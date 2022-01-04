from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    shipping_address = models.ForeignKey('Addresses', null=True,
                                         related_name='shipping_addr', on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        'Addresses', null=True, related_name='billing_addr', on_delete=models.CASCADE)


class Addresses(models.Model):
    street = models.TextField()
    street_number = models.IntegerField()
    postal_code = models.TextField()
    city = models.TextField()
    state_or_provence = models.TextField()
    country = models.TextField()
