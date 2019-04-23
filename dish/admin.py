from django.contrib import admin
from .models import Dish, DishType, Provider
# Register your models here.
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Provider)
