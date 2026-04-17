from django.contrib import admin
from .models import Tweet

# Register your models here.
admin.site.register(Tweet) # register the Tweet model with the admin site to make it accessible through the Django admin interface