from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import BlogPostForm
from django.utils.text import slugify

# Представления для главной страницы, страницы "О нас" и страницы "Контакты"
class HomeView(TemplateView):
    template_name = 'blog_project/home.html'

class AboutView(TemplateView):
    template_name = 'blog_project/about.html'

class ContactView(TemplateView):
    template_name = 'blog_project/contact.html'

# Представления для CRUD операций с моделью BlogPost
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_project/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_project/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog_project/blogpost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        counter = 1
        while BlogPost.objects.filter(slug=self.object.slug).exists():
            self.object.slug = f"{slugify(self.object.title)}-{counter}"
            counter += 1
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', args=[self.object.pk])

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog_project/blogpost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        counter = 1
        while BlogPost.objects.filter(slug=self.object.slug).exists():
            self.object.slug = f"{slugify(self.object.title)}-{counter}"
            counter += 1
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogpost_detail', args=[self.object.pk])

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_project/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')
