from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/manage-category/', views.category, name='manage-category'),
    path('dashboard/manage-category/add/',
         views.add_category, name='add-category'),

    path('dashboard/manage-news/', views.news, name='manage-news'),

    path('dashboard/trash/', views.trash, name='trash')
]
