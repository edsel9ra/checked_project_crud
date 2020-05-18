from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('code', 'description', 'presentation', 'corrugated_quantity')