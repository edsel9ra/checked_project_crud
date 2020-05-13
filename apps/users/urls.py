from django.contrib import admin
from django.urls import path
from apps.users.views import LoginView

app_name = 'users'

urlpatterns = [
    path('login',view=LoginView.as_view(),name=LoginView.name),
]
