from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name = 'cts'
urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login")
    url(r"^case/$", views.court_case, name="case"),
]