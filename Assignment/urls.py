"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from static.views import Home
from static.views import Signin
from static.views import Login
from static.views import Success
from static.views import Yes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='home'),
    path('signin.html/', Signin.as_view(),name='signin'),
    path('login.html/', Login.as_view(),name='login'),
    path('success.html/', Success.as_view(),name='success'),
    path('success.html/home.html', Home.as_view(),name='home'),
    path('signin.html/success.html', Success.as_view(),name='home'),
    path('signin.html/home.html', Home.as_view(),name='home'),
    path('signin.html/login.html', Login.as_view(),name='login'),
    path('signin.html/signin.html', Signin.as_view(),name='signin'),
    path('signin.html/success.php', Yes.as_view(),name='success'),

]
