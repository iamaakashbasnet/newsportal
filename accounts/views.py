from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from posts.models import Post


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
        'total_news': Post.objects.all().count(),
        'total_categories': Tag.objects.all().count()
    }
    return render(request, 'accounts/dashboard.html', context)


# Category ==========================

@login_required
def category(request):
    context = {
        'title': 'Manage Category',
        'categories': Tag.objects.all()
    }
    return render(request, 'accounts/category-manager/category.html', context)


@login_required
def add_category(request):
    context = {
        'title': 'Add Category'
    }
    return render(request, 'accounts/category-manager/add_category.html', context)


# News ==============================
def news(request):
    return render(request, 'accounts/news-manager/news.html')


# Trash ==============================
def trash(request):
    return render(request, 'accounts/trash/trash.html')
