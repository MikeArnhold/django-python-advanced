"""core models"""
from typing import Any

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from .utils import create_superuser


class UserManager(BaseUserManager):
    """custom user manager"""

    def create_user(
        self, email: str, password: str = None, **extra_fields: Any
    ) -> "User":
        """Creates and save new user"""

        if email is None:
            raise ValueError("User must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str) -> "User":
        """create new superuser"""

        return create_superuser(self.create_user, email, password)


class User(AbstractBaseUser, PermissionsMixin):
    """user

    Uses email instead of username
    """

    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
