from django.shortcuts import render, get_object_or_404

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


def goods(request, pk):
    object = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/goods.html', {'object': object})


# def goods(request, pk):
#     goods_list = Product.objects.filter(category_id=pk),
#     context = {
#         'objects_list': goods_list
#     }
#     return render(request, 'catalog/goods.html', context)
