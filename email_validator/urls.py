from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='email_validator_index'),
    path('validator', views.email_validator, name='email_validator')
]
