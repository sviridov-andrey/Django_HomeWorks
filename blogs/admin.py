from django.contrib import admin
from blogs.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('title',)
