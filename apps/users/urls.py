from django.contrib import admin
from django.urls import path, include
from apps.users.views import LoginView, UserCreate, LogoutView

app_name = 'users'

urlpatterns = [
    path('login', view=LoginView.as_view(), name=LoginView.name),
    path('create', view=UserCreate.as_view(), name=UserCreate.name),
    path('logout', view=LogoutView.as_view(), name='logout')
]
