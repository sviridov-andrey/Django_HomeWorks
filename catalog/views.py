from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    goods_list = Product.objects.all()
    context = {
        'objects_list': goods_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def goods(request):
    goods_list = Product.objects.all()
    context = {
        'objects_list': goods_list
    }
    return render(request, 'catalog/includes/goods.html', context)
