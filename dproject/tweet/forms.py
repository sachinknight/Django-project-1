from django import forms
from .models import Tweet # import the Tweet model to create a form based on it

class TweetForm(forms.ModelForm): #
    class Meta:
        model = Tweet # specify that this form is based on the Tweet model
        fields = ['text', 'photo'] # specify the fields to include in the form, which are 'text' and 'photo' from the Tweet model