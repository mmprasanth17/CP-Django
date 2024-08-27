from django import forms
from .models import user
from .models import Comment# Assuming 'user' is the model you are using

class AddForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Image', 'BikeName', 'Description','author','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
