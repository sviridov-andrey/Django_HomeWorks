from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request):
    return render(request, 'catalog/product.html')
