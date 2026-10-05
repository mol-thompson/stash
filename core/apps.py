"""Application configuration for the core app."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuration for the core app, which owns site-wide public pages."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
