from django.urls import path
from .views import CheckListCreate, CheckedProductUpdate, CheckProductList

app_name = 'checklist'

urlpatterns = [
     path('create', view=CheckListCreate.as_view(), name=CheckListCreate.name),
     path('check_product_update/<int:pk>', view=CheckedProductUpdate.as_view(), name=CheckedProductUpdate.name),
     path('checked_product_list', view=CheckProductList.as_view(), name=CheckProductList.name),
]