from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('q-explorer', views.question_explorer, name='question_explorer'),
    path('p-explorer', views.prepositional_explorer,
         name='prepositional_explorer'),
    path('c-explorer', views.comparison_explorer, name='comparions_explorer'),
    path('alpha-explorer', views.alpha_explorer, name='alpha_explorer'),
]
