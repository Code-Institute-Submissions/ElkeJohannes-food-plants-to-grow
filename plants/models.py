from django.db import models


class Plant(models.Model):
    Common_name = models.CharField(max_length=100, null=False, blank=False)
    Botanical_name = models.CharField(max_length=100, null=False, blank=False)
    Description = models.TextField()
    Stock = models.IntegerField(default=0, null=False, blank=False)
    Price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    Layer = models.CharField(max_length=100, choices=[
        ('Large trees', 'Large trees'), ('Medium trees', 'Medium trees'), 
        ('Small trees', 'Small trees'), ('Shrubs', 'Shrubs'),
        ('Ground covers', 'Ground covers'), ('Climbers', 'Climbers'),
        ('Roots', 'Roots')], null=False, blank=False)
    Image_url = models.URLField(max_length=1024, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Common_name
