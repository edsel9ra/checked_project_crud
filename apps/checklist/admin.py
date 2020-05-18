from django.contrib import admin
from .models import CheckList,CheckedProduct

# Register your models here.

@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    pass


@admin.register(CheckedProduct)
class CheckProductAdmin(admin.ModelAdmin):
    pass