from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('researcher', views.keyword_researcher, name='keyword_researcher'),
]
