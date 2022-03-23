from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('yt-q-explorer', views.yt_question_explorer,
         name='yt_question_explorer'),
    path('yt-p-explorer', views.yt_prepositional_explorer,
         name='yt_prepositional_explorer'),
    path('yt-c-explorer', views.yt_comparison_explorer,
         name='yt_comparions_explorer'),
    path('yt-alpha-explorer', views.yt_alpha_explorer, name='yt_alpha_explorer'),
]
