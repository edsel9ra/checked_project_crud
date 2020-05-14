from django.shortcuts import render
from django.views.generic import TemplateView
from apps.users.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class LoginView(TemplateView):
    name = 'login'
    template_name = 'users/login.html'

    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(
            request,
            self.template_name,
            {
                'form':form
            }
        )
    
    def post(self,request,*args,**kwargs):
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

        user = authenticate(request,username=data.get('username'),password=data.get('password'))

        if not user:
            return render(
                request,
                self.template_name,
                {
                    'form':
                    form
                }
            )

        login(request,user)

        back = request.GET.get('next')

        if back:
            return HttpResponseRedirect(back)
            
        return redirect('product:list')

        


