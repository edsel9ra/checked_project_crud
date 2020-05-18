from django.urls import path, include
from .views import CheckListCreate

app_name = 'checklist'

urlpatterns = [
     path('create',view=CheckListCreate.as_view(),name=CheckListCreate.name)
]