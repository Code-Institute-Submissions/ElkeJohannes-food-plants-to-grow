from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import DateField
from plants.models import Plant
from accounts.models import Users

class Orders(models.Model):
    plant_id = models.ForeignKey(Plant, null=True, on_delete=SET_NULL)
    user_id = models.ForeignKey(Users, null=True, on_delete=SET_NULL)
    date = models.DateField()
    shipping_fee = models.DecimalField(decimal_places=2, max_digits=6)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)
