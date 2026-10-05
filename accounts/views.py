"""Views for the accounts app."""

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """Account dashboard shell view."""

    template_name = "accounts/dashboard.html"
