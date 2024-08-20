from django import forms
from .models import Review


# class Feedbackform(forms.Form):
#     user_name = forms.CharField(label='Enter the name', max_length =50,min_length=3,required=True,
#     error_messages={
#         'required':'It is Empty Value',
#          'max_length': 'Name cannot exceed 20 characters',
#          'min_length':'give less word'
#     })
#     text = forms.CharField(label='Enter the Feedback',widget=forms.Textarea)
#     rating = forms.IntegerField(label='Enter the Rating',min_value=1,max_value=5)
    

class Feedbackform(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['user_name',rating]
        #exclude = []
        labels = {
            'user_name':'Your Name'
        }  