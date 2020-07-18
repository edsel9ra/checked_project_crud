#from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from .models import Product
from .forms import ProductForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@method_decorator(login_required,name='dispatch')
class ProductList(ListView):
    name = 'list'
    model = Product

@method_decorator(login_required,name='dispatch')
class ProductCreate(CreateView):
    name = 'create'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('product:list')

@method_decorator(login_required,name='dispatch')
class ProductUpdate(UpdateView):
    name = 'update'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('product:list')

