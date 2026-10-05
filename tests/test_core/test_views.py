"""Tests for the core app's site-wide views."""

from django.test import Client
from django.urls import reverse


def test_home_page_is_publicly_accessible(client: Client) -> None:
    """The homepage renders with HTTP 200 for anonymous visitors."""
    response = client.get(reverse("core:home"))

    assert response.status_code == 200


def test_home_page_renders_the_stash_landing_content(client: Client) -> None:
    """The homepage renders the core home template with branding and auth CTAs."""
    response = client.get(reverse("core:home"))

    template_names = [template.name for template in response.templates]
    assert "core/home.html" in template_names
    assert "base.html" in template_names

    content = response.content.decode("utf-8")
    assert "Stash" in content
    assert "/auth/signup/" in content
    assert "/auth/login/" in content
