from django import forms
from .models import user  # Assuming 'user' is the model you are using

class AddForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Image', 'BikeName', 'Description',]
