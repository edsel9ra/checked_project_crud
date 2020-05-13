from django.shortcuts import render
from django.views.generic import TemplateView
from apps.users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class HomeView(TemplateView):
    name = 'home'
    template_name = 'commons/home.html'


