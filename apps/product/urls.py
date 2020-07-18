from django.urls import path
from .views import ProductList, ProductUpdate, ProductCreate

app_name = 'product'

urlpatterns = [
     path('list',view=ProductList.as_view(),name=ProductList.name),
     path('create',view=ProductCreate.as_view(),name=ProductCreate.name),
     path('update/<int:pk>',view=ProductUpdate.as_view(),name=ProductUpdate.name)
]