from django import forms
from django.utils.translation import ugettext as _
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label=_('Usuario'),max_length=40,min_length=1)
    password = forms.CharField(label=_('Contraseña'),widget=forms.PasswordInput,min_length=1)

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('code', 'first_name', 'last_name', 'username', 'area', 'birth_date', 'is_base')
    
