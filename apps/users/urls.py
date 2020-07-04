from django.contrib import admin
from django.urls import path, include
from apps.users.views import LoginView, UserCreate

app_name = 'users'

urlpatterns = [
    path('login', view=LoginView.as_view(), name=LoginView.name),
    path('create', view=UserCreate.as_view(), name=UserCreate.name),
]
