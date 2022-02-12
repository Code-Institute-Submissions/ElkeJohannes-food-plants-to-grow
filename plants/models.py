from django.db import models


class Plant(models.Model):
    common_name = models.CharField(max_length=100, null=False, blank=False)
    botanical_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    stock = models.IntegerField(default=0, null=False, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.common_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
