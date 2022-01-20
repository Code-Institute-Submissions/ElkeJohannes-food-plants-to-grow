from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField

class UserAccount(AbstractUser):
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
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
    