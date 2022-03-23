from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='text_summarizer_index'),
    path('text-summarizer', views.text_summarizer, name='text_summarizer'),
]
