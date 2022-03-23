from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hash_generator_index'),
    path('generator', views.hash_generator, name='hash_generator'),
]
