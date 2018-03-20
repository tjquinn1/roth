from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name = 'cts'
urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login")
    url(r"^case/$", views.court_case, name="case"),
    url(r"^abuse/(?P<client_id>\d+)/(?P<program_id>\d+)/$", views.abuse, name="abuse"),
    url(r"^psych/(?P<program_id>\d+)/$", views.psych, name="psych"),
    url(r"^mast/(?P<program_id>\d+)/$", views.mast, name="mast"),
    url(r"^upload_client/$", views.upload_client, name="upload_client"),
    url(r"^upload_mast/$", views.upload_mast, name="upload_mast"),
    url(r"^upload_fin/$", views.upload_fin, name="upload_fin"),
    url(r"^upload_psych/$", views.upload_psych, name="upload_psych"),
    url(r"^upload_abuse/$", views.upload_abuse, name="upload_abuse"),
    url(r"^upload_program/$", views.upload_program, name="upload_program"),
]