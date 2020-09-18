from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name  = 'common/home.html'


class Signin(TemplateView):
    template_name  = 'common/signin.html'

    
class Login(TemplateView):
    template_name  = 'common/login.html'

class Success(TemplateView):
    template_name  = 'common/success.html'

class Yes(TemplateView):
    template_name  = 'common/success.php'
