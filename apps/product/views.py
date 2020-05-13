from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    contexto = {'product_list': Product.objects.all()}
    return render(request, "product/product_list.html", contexto)


def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request, "producto/product_form.html", {'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/product/list')


def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/product/list')
