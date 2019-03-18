from django.db import models


class DishType(models.Model):
    name = models.CharField(default='', max_length=256)
    # salad price is in dishes
    #
    generic_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(default='Default Dish', max_length=256)
    type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, default='default')
    cost = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + ' - ' + self.type.name

class Set(models.Model):
    name = models.CharField(default='Default Set', max_length=256)
    price = models.FloatField(default=0.0)

