from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='domain_name_index'),
    path('dn-checker-generator', views.domain_name_checker,
         name='domain_name_checker')
]
