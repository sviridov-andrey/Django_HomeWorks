from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, VersionForm
from .models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        print(context_data['formset'])
        return context_data


class ProdictListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        version_list = Version.objects.all()
        context_data['formset'] = version_list
        return context_data


class ProductContactListView(ListView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/goods.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog:index')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')


