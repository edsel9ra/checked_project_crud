#from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import CheckList, CheckedProduct
from .forms import CheckListForm, CheckedProductFormSet, CheckedProductForm


@method_decorator(login_required, name='dispatch')
class CheckProductList(ListView):
    name = 'checked_product_list'
    model = CheckedProduct
    paginate_by = 5 #22 original del formato


@method_decorator(login_required, name='dispatch')
class CheckListCreate(CreateView):
    name = 'create'
    model = CheckList
    form_class = CheckListForm

    def get_success_url(self):
        return reverse_lazy('checklist:checked_product_list')

    def get_checkedproduct_form_kwargs(self):
        if self.request.method in ('POST', 'PUT'):
            return CheckedProductFormSet(instance=self.object, prefix='checkedproduct', data=self.request.POST, files=self.request.FILES)
        else:
            return CheckedProductFormSet(instance=self.object, prefix='checkedproduct')

    def get_context_data(self, **kwargs):
        context = super(CheckListCreate, self).get_context_data()
        context['formset_checkedproduct'] = self.get_checkedproduct_form_kwargs()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()

        if form.is_valid():
            form.instance.deliver = self.request.user
            response = self.form_valid(form)
        else:
            return self.form_invalid(form)

        formset = self.get_checkedproduct_form_kwargs()

        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)

        return response


@method_decorator(login_required, name='dispatch')
class CheckListUpdate(UpdateView):
    name = 'check_list_update'
    model = CheckList
    form_class = CheckListForm
    
    def get_success_url(self):
        return reverse_lazy('checklist:checked_product_list')


@method_decorator(login_required, name='dispatch')
class CheckedProductUpdate(UpdateView):
    name = 'check_product_update'
    model = CheckedProduct
    form_class = CheckedProductForm

    def get_success_url(self):
        return reverse_lazy('checklist:checked_product_list')