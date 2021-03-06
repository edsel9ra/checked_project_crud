from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from apps.users.forms import LoginForm, UserForm
from .models import User

class LoginView(TemplateView):
    name = 'login'
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    'form':
                    form
                }
            )

        data = form.cleaned_data

        user = authenticate(request, username=data.get(
            'username'), password=data.get('password'))

        if not user:
            return render(
                request,
                self.template_name,
                {
                    'form':
                    form
                }
            )

        login(request, user)

        back = request.GET.get('next')

        if back:
            return HttpResponseRedirect(back)

        return redirect('checklist:checked_product_list')


@method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):
    name = 'create'
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('checklist:checked_product_list')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('users:login')
