from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='article_rewiter_index'),
    path('rewriter', views.article_rewiter, name='article_rewiter')
]
