from django import forms
from .models import Product, CheckList


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('code', 'description', 'presentation', 'corrugated_quantity')

class CheckListForm(forms.ModelForm):

    class Meta:
        model = CheckList
        fields = ('product', 'packing_list', 'quantity', 'receiver', 'deliver', 'check_date')
