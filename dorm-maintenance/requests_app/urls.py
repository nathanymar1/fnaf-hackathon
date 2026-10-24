# requests_app/urls.py  (new file you create)
from django.urls import path
from . import views

app_name = "requests_app"

urlpatterns = [
    path("dashboard/", views.request_dashboard, name="list"),
    path("submit/", views.request_form, name="submit"),
]