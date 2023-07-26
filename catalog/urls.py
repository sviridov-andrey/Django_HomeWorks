from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProdictListView, ProductDetailView, ProductContactListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProdictListView.as_view(), name='index'),
    path('contacts/', ProductContactListView.as_view(), name='contacts'),
    path('goods/<int:pk>/', ProductDetailView.as_view(), name='goods'),
]
