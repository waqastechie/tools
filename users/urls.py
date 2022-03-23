from users.views import dashboard, signup, activate
from users.views import dashboard
from django.conf.urls import include, url
from django.urls import path
from users import views

# users/urls.py


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", signup, name="register"),
    path(r'^activate/<uidb64>/<token>/', views.activate, name='activate'),
]
