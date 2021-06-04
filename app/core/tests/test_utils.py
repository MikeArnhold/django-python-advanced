"""test utils"""
from typing import Optional, Tuple

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.test import TestCase

from ..utils import create_superuser

UserModel = get_user_model()


class CreateSuperuserTests(TestCase):
    """create superuser tests"""

    def test_uses_create_callback(self) -> None:
        """uses create callback"""

        user = UserModel()

        def mock_create(
            email: str,
            password: str,
            is_staff: bool = None,
            is_superuser: bool = None,
        ) -> AbstractBaseUser:
            return user

        super_user = create_superuser(
            mock_create,
            "test@test.com",
            "Password123",
        )

        self.assertEqual(super_user, user)

    def test_passes_arguments_to_create(self) -> None:
        """arguments are passed to create callback"""

        TPassed = Tuple[str, str, Optional[bool], Optional[bool]]

        passed: TPassed = ("", "", None, None)
        email = "test@test.com"
        passw = "Password123"

        def mock_create(
            email: str,
            password: str,
            is_staff: bool = None,
            is_superuser: bool = None,
        ) -> AbstractBaseUser:
            nonlocal passed
            passed = (email, password, is_staff, is_superuser)
            return UserModel()

        create_superuser(mock_create, email, passw)

        self.assertEqual((email, passw, True, True), passed)
