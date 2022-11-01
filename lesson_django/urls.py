
from django.contrib import admin
from django.template.defaultfilters import random
from django.urls import path, include
from django.views.generic import DetailView

from myapp import views


urlpatterns = [

    path('', views.first, name='first'),
    path('first_page/', views.index, name='index'),
    path('random_id/<int:id>/', views.random_id, name='random_id'),
    path('slug/<slug:slug>/', views.r_slug, name='slug'),
    path('article/', views.article, name='article'),
    path('article/', include('myapp.urls')),
    path('articles/', views.articles, name='articles'),
    path('articles/archive/', views.archive, name='archive'),
    path('users/', views.users, name='users'),
    path('<int:user_number>/', views.users, name='users_id'),

]
