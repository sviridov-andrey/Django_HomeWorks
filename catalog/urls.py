from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProdictListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProdictListView.as_view(), name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('goods/<int:pk>/', ProductDetailView.as_view(), name='goods'),
]
