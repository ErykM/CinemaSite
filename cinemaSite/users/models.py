from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


def create_superuser(self, email, name, password, **kwargs):
    kwargs.setdefault('is_super', True)

    if kwargs.get('is_super') is not True:
        raise ValueError(
            'Superuser must have flag is_super assigned to True'
        )
    return self.create_superuser(email, name, password, **kwargs)


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, name, password, **kwargs):
        if not email:
            raise ValueError('You must provide email address')
        email = self.normalize_email(email)

        user = self.model(email=email, name=name, **kwargs)
        user.set_password(password)
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=100)
    is_super = models.BooleanField(default=False)

    USERNAME_FIELD = email
    REQUIRED_FIELDS = [email]

    def __str__(self):
        return self.name
