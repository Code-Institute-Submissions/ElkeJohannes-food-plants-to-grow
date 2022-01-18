from email.policy import default
from django.db import models


class Suggestion(models.Model):
    common_name = models.CharField(max_length=100, null=False, blank=False)
    botanical_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    number_of_upvotes = models.IntegerField(default=0)
