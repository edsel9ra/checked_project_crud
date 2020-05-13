from django.contrib import admin
from django.urls import path
from apps.commons.views import HomeView

app_name = 'commons'

urlpatterns = [
    path('',view=HomeView.as_view(),name=HomeView.name),
]
