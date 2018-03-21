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
    url(r"^mast/(?P<program_id>\d+)/(?P<client_id>\d+)/$", views.mast, name="mast"),
    url(r"^upload_client/$", views.upload_client, name="uploadClient"),
    url(r"^upload_mast/$", views.upload_mast, name="uploadMast"),
    url(r"^upload_fin/$", views.upload_fin, name="uploadFin"),
    url(r"^upload_psych/$", views.upload_psych, name="uploadPsych"),
    url(r"^upload_abuse/$", views.upload_abuse, name="uploadAbuse"),
    url(r"^upload_program/$", views.upload_program, name="uploadProgram"),
]