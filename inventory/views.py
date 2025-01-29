from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect


from .models import Product
from .forms import ProductForm

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