from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:view', kwargs={'slug': self.object.slug})


class BlogListView(ListView):
    model = Blog
    context_object_name = 'objects_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:view', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/catalog_confirm_delete.html'
    success_url = reverse_lazy('blogs:list')
