"""Views for core site-wide pages."""

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from global_login_required import login_not_required


@method_decorator(login_not_required, name="dispatch")
class HomeView(TemplateView):
    """Public landing page introducing Stash and linking into the application."""

    template_name = "core/home.html"
