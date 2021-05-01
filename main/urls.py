from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeNewsListView.as_view(), name='home'),
    path('news-detail/<slug:slug>/',
         views.NewsDetailView.as_view(), name='news-detail'),
    path('category/<slug:slug>/',
         views.CategoryNewsListView.as_view(), name='category'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about')
]
