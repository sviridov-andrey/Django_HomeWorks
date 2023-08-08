from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProdictListView, ProductDetailView, ProductContactListView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProdictListView.as_view(), name='index'),
    path('contacts/', ProductContactListView.as_view(), name='contacts'),
    path('goods/<int:pk>/', ProductDetailView.as_view(), name='goods'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('version_create/', VersionCreateView.as_view(), name='version_create'),
]
