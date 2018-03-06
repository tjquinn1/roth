from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views
app_name = 'accounts'
urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login"),
    url(r"^logout/$", views.logout_view, name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r'edit/$', views.Edit, name='edit'),
    url(r'^login/$', views.custom_login, name='login'),
]