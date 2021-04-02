from django.urls import path
from . import views

urlpatterns = [
    path('', views.views_counter_manager, name='views-manager')
]
