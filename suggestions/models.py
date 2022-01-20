from django.db import models
from accounts.models import Account


class Suggestion(models.Model):
    common_name = models.CharField(max_length=100, null=False, blank=False)
    botanical_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    argument = models.TextField(null=True, blank=True)
    number_of_upvotes = models.IntegerField(default=0)
    upvoters = models.ManyToManyField(Account)

    def __str__(self):
        return self.common_name
