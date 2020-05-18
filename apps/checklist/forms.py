from django import forms
from .models import CheckList, CheckedProduct

class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ('receiver', 'check_date')

class CheckedProductForm(forms.ModelForm):
    class Meta:
        model = CheckedProduct
        fields = ('product','packing_list','quantity')

CheckedProductFormSet = forms.inlineformset_factory(CheckList,CheckedProduct,CheckedProductForm,can_delete=True,extra=1)
