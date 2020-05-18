from django.urls import path, include
from .views import ProductList ,ProductUpdate

app_name = 'product'

urlpatterns = [
     path('list',view=ProductList.as_view(),name=ProductList.name),
     path('update/<int:pk>',view=ProductUpdate.as_view(),name=ProductUpdate.name)
]