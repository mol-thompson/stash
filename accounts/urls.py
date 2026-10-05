"""URL configuration for the accounts app."""

from django.urls import path

from accounts.views import DashboardView

app_name = "accounts"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
