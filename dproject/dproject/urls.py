"""
URL configuration for dproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views  # Import Django's built-in authentication views for login and logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tweet/", include("tweet.urls")),
    # for account
    path("accounts/", include("django.contrib.auth.urls")),  # Include Django's built-in authentication URLs for login, logout, password reset, etc.
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
