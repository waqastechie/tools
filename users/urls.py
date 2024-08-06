from users.views import dashboard, signup, activate
from users.views import dashboard
from django.urls import include, re_path
from django.urls import path
from users import views

# users/urls.py


urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^register/", signup, name="register"),
    path(r'^activate/<uidb64>/<token>/', views.activate, name='activate'),
]
