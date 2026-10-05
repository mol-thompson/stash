"""Tests for the accounts app's custom user model."""

import pytest

from accounts.models import User


@pytest.mark.django_db
def test_user_string_uses_full_name_when_available() -> None:
    """A user's full name is used as their display string."""
    user = User.objects.create_user(
        username="molly",
        email="molly@example.com",
        password="test-password",
        first_name="Molly",
        last_name="Thompson",
    )

    assert str(user) == "Molly Thompson"


@pytest.mark.django_db
def test_user_string_falls_back_to_email_without_a_name() -> None:
    """A user's email is used as the display string when no name is set."""
    user = User.objects.create_user(
        username="molly",
        email="molly@example.com",
        password="test-password",
    )

    assert str(user) == "molly@example.com"


def test_user_email_is_required_and_unique() -> None:
    """The custom user model requires a unique email address."""
    email_field = User._meta.get_field("email")

    assert email_field.blank is False
    assert email_field.unique is True
