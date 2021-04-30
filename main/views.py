from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post


class HomeNewsListView(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(deleted=False)


class NewsDetailView(DetailView):
    model = Post
    template_name = 'main/news-detail.html'
    context_object_name = 'post'


class CategoryNewsListView(ListView):
    model = Post
    template_name = 'main/category-newslist.html'
    context_object_name = 'posts'

    def get_queryset(self):
        print(self.request.GET.get('slug'))
        return Post.objects.filter(tags=self.request.GET.get('slug'))
