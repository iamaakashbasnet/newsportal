import json
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag
from posts.models import Post, ViewCounter
from datetime import datetime


def admin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'total_news': Post.objects.count(),
        'total_categories': Tag.objects.count(),
        'total_views': ViewCounter.objects.get(day=int(datetime.now().strftime('%d'))).views,
        'views_list': json.dumps([i.views for i in ViewCounter.objects.all()])
    }

    return render(request, 'accounts/dashboard.html', context)


# Category ==========================

class CategoryListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'accounts/category-manager/category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Category'
        return data


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name']
    template_name = 'accounts/category-manager/add_category.html'
    success_url = reverse_lazy('manage-category')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Add Category'
        return data


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'slug']
    template_name = 'accounts/category-manager/update_category.html'
    success_url = reverse_lazy('manage-category')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update Category'
        return data


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('manage-category')


# News ==============================

class NewsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'accounts/news-manager/news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'News'
        return data


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'desc', 'tags']
    template_name = 'accounts/news-manager/add_news.html'
    success_url = reverse_lazy('manage-news')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Add News'
        return data


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'desc', 'tags']
    template_name = 'accounts/news-manager/update_news.html'
    success_url = reverse_lazy('manage-news')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Update News'
        return data


class NewsPermDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('manage-news')


@login_required
def news_delete_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.deleted = True
    post.save()

    return redirect('manage-news')


@login_required
def news_restore_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.deleted = False
    post.save()

    return redirect('manage-news')


# Trash ==============================

def trash(request):
    context = {
        'posts': Post.objects.filter(deleted=True)
    }
    return render(request, 'accounts/trash/trash.html', context)
