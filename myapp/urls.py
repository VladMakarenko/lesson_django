from django.urls import path

from myapp.views import article

urlpatterns = [

    path('<int:article_number>/', article, name='article_id'),
    path('<int:article_number>/<slug:slug_text>/', article, name='article_2'),

]
