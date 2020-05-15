from django.urls import path, include
from apps.product.views import ProductList ,ProductUpdate, CheckOutList, CheckListCreate, CheckListUpdate

app_name = 'product'

urlpatterns = [
     path('list',view=ProductList.as_view(),name=ProductList.name),
     path('update/<int:pk>',view=ProductUpdate.as_view(),name=ProductUpdate.name),
     path('check_out_list',view=CheckOutList.as_view(),name=CheckOutList.name),
     path('check_list_create',view=CheckListCreate.as_view(),name=CheckListCreate.name),
     path('check_list_update/<int:pk>',view=CheckListUpdate.as_view(),name=CheckListUpdate.name),
]