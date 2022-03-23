from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cwv-engine', views.engine, name='engine'),
]
