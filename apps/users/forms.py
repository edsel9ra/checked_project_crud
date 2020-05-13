from django import forms
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
    username = forms.CharField(label=_('Usuario'),max_length=40,min_length=1)
    password = forms.CharField(label=_('Contraseña'),widget=forms.PasswordInput,min_length=1)