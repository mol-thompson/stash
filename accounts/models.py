"""Models for the accounts app."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model for Stash."""

    email = models.EmailField(unique=True, blank=False)

    def __str__(self) -> str:
        """Return the user's display name."""
        return f"{self.first_name} {self.last_name}".strip() or self.email
