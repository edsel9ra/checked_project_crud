from django.urls import path, include
from .views import CheckListCreate, CheckListUpdate, CheckOutList, CheckedProductUpdate, CheckProductList

app_name = 'checklist'

urlpatterns = [
     path('create', view=CheckListCreate.as_view(),name=CheckListCreate.name),
     path('check_list_update/<int:pk>', view=CheckListUpdate.as_view(), name=CheckListUpdate.name),
     path('check_product_update/<int:pk>', view=CheckedProductUpdate.as_view(), name=CheckedProductUpdate.name),
     path('list', view=CheckOutList.as_view(), name=CheckOutList.name),
     path('checked_product_list/<int:pk>', view=CheckProductList.as_view(), name=CheckProductList.name),
]