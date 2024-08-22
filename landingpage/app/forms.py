from django import forms
from .models import user

class ProductForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['image', 'product_name', 'description', 'cost', 'rating']
