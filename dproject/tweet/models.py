from django.db import models # import the models module from Django's database library to define the structure of the Tweet model
from django.contrib.auth.models import User # import the built-in User model from Django's authentication system to establish a relationship between tweets and users

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # one user can have many tweets, but one tweet belongs to one user
    text = models.TextField(max_length=240) # the text of the tweet, with a maximum length of 240 characters
    photo = models.ImageField(upload_to='photos/', blank=True, null=True) # optional field for photo upload
    created_at = models.DateTimeField(auto_now_add=True) # automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # automatically set the field to now every time the object is saved

    def __str__(self): # define the string representation of the model for easy identification in the admin panel
        return f'{self.user.username} - {self.text[:10]}' # return the username and the first 10 characters of the tweet text for easy identification in the admin panel
    