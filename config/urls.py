"""Project-level URL configurations."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("site-admin/", admin.site.urls),
    path("auth/", include("allauth.urls")),
    path("", include("core.urls")),
    path("account/", include("accounts.urls")),
]

handler400 = "config.error_handlers.handler400"
handler403 = "config.error_handlers.handler403"
handler404 = "config.error_handlers.handler404"
handler500 = "config.error_handlers.handler500"
