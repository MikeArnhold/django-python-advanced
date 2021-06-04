"""Model tests"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """model tests"""

    def test_create_user_with_email_successful(self) -> None:
        """create new user with email is succesfull"""

        email = "test@test.com"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normaliced(self) -> None:
        """new user email is normalized"""

        email = "Test@TEST.com"

        user = get_user_model().objects.create_user(
            email=email,
            password="Testpass123",
        )

        self.assertEqual(user.email, "Test@test.com")

    def test_new_user_invalid_email(self) -> None:
        """new user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="Testpass123",
            )

    def test_create_new_superuser(self) -> None:
        """create new superuser"""

        user = get_user_model().objects.create_superuser(
            email="test@test.com",
            password="Testpass123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
