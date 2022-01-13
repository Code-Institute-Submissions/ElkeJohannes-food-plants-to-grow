from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_name = models.CharField(max_length=80, null=False, blank=False)
    street_number = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    