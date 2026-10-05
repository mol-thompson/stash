"""URL configuration for core site-wide pages."""

from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
