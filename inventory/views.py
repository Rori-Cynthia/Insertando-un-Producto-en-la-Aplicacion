from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

from .forms import ProductForm
from .models import Product


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductInputView(FormView):
    form_class = ProductForm
    template_name = 'add_product.html'
    context_object_name = 'products'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Has añadido un producto exitosamente.')
        return redirect('list_product')


class ProductListView(ListView):
    model = Product
    template_name = 'list_product.html'
    context_object_name = 'products'