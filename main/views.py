from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post


class HomeNewsListView(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    paginate_by = 1

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
    paginate_by = 1

    def get_queryset(self):
        print(self.kwargs['slug'])
        return Post.objects.filter(tags__slug=self.kwargs['slug']).distinct()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = self.kwargs['slug']
        return data


def search(request):
    if request.method == 'POST':
        q = request.POST.get('q')
        results = Post.objects.filter(title__contains=q)
        context = {
            'results': results,
            'q': q
        }
        return render(request, 'main/search_results.html', context)


def about(request):
    return render(request, 'main/about.html')
