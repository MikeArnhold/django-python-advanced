"""core utils"""
from typing import Callable

from django.contrib.auth.models import AbstractBaseUser

UserCreateFunc = Callable[..., AbstractBaseUser]


def create_superuser(
    create: UserCreateFunc,
    email: str,
    password: str,
) -> AbstractBaseUser:
    """create new superuser via the provided create callback"""
    user = create(email, password, is_staff=True, is_superuser=True)
    return user
