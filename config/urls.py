"""Project-level URL configurations."""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("site-admin/", admin.site.urls),
]
