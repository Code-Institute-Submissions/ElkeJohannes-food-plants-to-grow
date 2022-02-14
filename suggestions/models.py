from django.db import models


class Suggestion(models.Model):
    common_name = models.CharField(max_length=100, null=False, blank=False)
    botanical_name = models.CharField(max_length=100, null=False,
                                      blank=False, unique=True)
    argument = models.TextField(null=True, blank=True)
    number_of_upvotes = models.IntegerField(default=0)
    upvoters = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.common_name
    
    def upvoters_as_list(self):
        list_of_upvoters = str(self.upvoters).split(';')
        return list_of_upvoters
