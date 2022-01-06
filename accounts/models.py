from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    shipping_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    shipping_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    shipping_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    shipping_county = models.CharField(max_length=80, null=True, blank=True)
    shipping_postcode = models.CharField(max_length=20, null=True, blank=True)
    shipping_country = CountryField(blank_label='Country', null=True, blank=True)
    billing_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    billing_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    billing_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    billing_country = CountryField(blank_label='Country', null=True, blank=True)
