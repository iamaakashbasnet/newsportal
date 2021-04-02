from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.admin),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('dashboard/manage-category/',
         views.CategoryListView.as_view(), name='manage-category'),

    path('dashboard/manage-category/add/',
         views.CategoryCreateView.as_view(), name='add-category'),

    path('dashboard/manage-category/<int:pk>/update/',
         views.CategoryUpdateView.as_view(), name='update-category'),

    path('dashboard/manage-category/<int:pk>/delete/',
         views.CategoryDeleteView.as_view(), name='delete-category'),

    path('dashboard/manage-news/', views.NewsListView.as_view(), name='manage-news'),

    path('dashboard/manage-news/add/',
         views.NewsCreateView.as_view(), name='add-news'),

    path('dashboard/manage-news/<int:pk>/update/',
         views.NewsUpdateView.as_view(), name='update-news'),

    path('dashboard/manage-news/<int:pk>/delete/',
         views.news_delete_view, name='delete-news'),

    path('dashboard/manage-news/<int:pk>/restore/',
         views.news_restore_view, name='restore-news'),

    path('dashboard/manage-news/<int:pk>/delete-news-perm/',
         views.NewsPermDeleteView.as_view(), name='delete-news-perm'),

    path('dashboard/trash/', views.trash, name='trash')
]
