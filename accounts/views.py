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
from posts.models import Post


def admin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return redirect('login')


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'total_news': Post.objects.all().count(),
        'total_categories': Tag.objects.all().count()
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

def news(request):
    return render(request, 'accounts/news-manager/news.html')


# Trash ==============================

def trash(request):
    return render(request, 'accounts/trash/trash.html')
