from django import forms
from .models import Dish, DishType

class DishForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Dish
        fields = ['name', 'type', 'description']