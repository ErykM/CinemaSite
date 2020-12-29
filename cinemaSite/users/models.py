from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, name, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have flag is_staff assigned to True'
            )

        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have flag is_superuser assigned to True'
            )
        return self.create_user(email, name, password, **kwargs)

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
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
