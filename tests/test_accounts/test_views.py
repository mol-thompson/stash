"""Tests for account authentication and the dashboard."""

import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import User


@pytest.mark.django_db
def test_signup_creates_user_without_username_input(client: Client) -> None:
    """Email-only signup creates and authenticates a user."""
    response = client.post(
        reverse("account_signup"),
        {
            "email": "developer@example.com",
            "password1": "a-strong-test-password",
            "password2": "a-strong-test-password",
        },
    )

    user = User.objects.get(email="developer@example.com")
    assert response.status_code == 302
    assert user.username
    assert "_auth_user_id" in client.session


@pytest.mark.django_db
def test_signup_rejects_an_email_that_is_already_registered(client: Client) -> None:
    """A second account cannot be registered with an existing email."""
    User.objects.create_user(
        username="existing",
        email="developer@example.com",
        password="a-strong-test-password",
    )

    response = client.post(
        reverse("account_signup"),
        {
            "email": "developer@example.com",
            "password1": "another-strong-test-password",
            "password2": "another-strong-test-password",
        },
    )

    assert response.status_code == 200
    assert User.objects.filter(email="developer@example.com").count() == 1
    assert "_auth_user_id" not in client.session


@pytest.mark.django_db
def test_login_accepts_email_address(client: Client) -> None:
    """Users can log in with their email address rather than username."""
    User.objects.create_user(
        username="developer",
        email="developer@example.com",
        password="a-strong-test-password",
    )

    response = client.post(
        reverse("account_login"),
        {
            "login": "developer@example.com",
            "password": "a-strong-test-password",
        },
    )

    assert response.status_code == 302
    assert "_auth_user_id" in client.session


@pytest.mark.django_db
def test_logout_ends_the_authenticated_session(client: Client) -> None:
    """A signed-in user can log out using the shared navigation form."""
    user = User.objects.create_user(
        username="developer",
        email="developer@example.com",
        password="a-strong-test-password",
    )
    client.force_login(user)

    response = client.post(reverse("account_logout"))

    assert response.status_code == 302
    assert "_auth_user_id" not in client.session


def test_dashboard_redirects_anonymous_visitors(client: Client) -> None:
    """Anonymous visitors are redirected to the Allauth login page."""
    response = client.get(reverse("accounts:dashboard"))

    assert response.status_code == 302
    assert response.url.startswith(f"{reverse('account_login')}?")


@pytest.mark.django_db
def test_dashboard_renders_for_authenticated_user(client: Client) -> None:
    """The dashboard renders its shell and authenticated navigation."""
    user = User.objects.create_user(
        username="developer",
        email="developer@example.com",
        password="a-strong-test-password",
    )
    client.force_login(user)

    response = client.get(reverse("accounts:dashboard"))

    assert response.status_code == 200
    assert "accounts/dashboard.html" in [
        template.name for template in response.templates
    ]
    assert b"Your stash is ready" in response.content
    assert b"My stash" in response.content
    assert b"Log out" in response.content
    assert b"Log in" not in response.content
    assert b'name="csrfmiddlewaretoken"' in response.content


def test_authentication_page_is_public(client: Client) -> None:
    """The global login requirement leaves Allauth login publicly accessible."""
    response = client.get(reverse("account_login"))

    assert response.status_code == 200


def test_admin_login_page_is_public(client: Client) -> None:
    """The global login requirement leaves the Django admin login public."""
    response = client.get(reverse("admin:login"))

    assert response.status_code == 200
