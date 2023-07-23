from django.urls import path
from . import views
from .apps import BlogsConfig
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView

app_name = BlogsConfig.name



urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),
 ]