from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProdictListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'objects_list'


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/goods.html'
