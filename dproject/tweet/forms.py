from django import forms
from .models import Tweet # import the Tweet model to create a form based on it
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm): #
    class Meta:
        model = Tweet # specify that this form is based on the Tweet model
        fields = ['text', 'photo'] # specify the fields to include in the form, which are 'text' and 'photo' from the Tweet model

class UserRegistrationForm(UserCreationForm): # create a custom user registration form that inherits from Django's built-in UserCreationForm
    email = forms.EmailField(required=True) # add an email field to the registration form, making it a required field for users to provide their email address during registration

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user