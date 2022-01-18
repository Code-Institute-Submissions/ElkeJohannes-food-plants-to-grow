from email.policy import default
from django.db import models


class Suggestion(models.Model):
    common_name = models.CharField(max_length=100, null=False, blank=False)
    botanical_name = models.CharField(max_length=100, null=False, blank=False)
    argument = models.TextField(null=True, blank=True)
    number_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.common_name
