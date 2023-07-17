from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def goods(request):
    goods_list = Product()
    context = {
        'goods_name': goods_list.product_name
    }
    return render(request, 'catalog/goods.html', context)
