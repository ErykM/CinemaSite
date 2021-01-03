import pytest

from users.models import CustomUser


@pytest.mark.django_db
class TestCustomUser:
    def test_create_user(self):
        name = 'unit_user'
        email = 'unit@user.com'
        user = CustomUser.objects.create_user(name=name, email=email, password='unit_password')
        assert user.name == name
        assert user.email == email
        assert user.is_active is True

    def test_create_superuser(self):
        name = 'super_user'
        email = 'super@user.com'
        user = CustomUser.objects.create_superuser(name=name, email=email, password='super_password')
        assert user.name == name
        assert user.email == email
        assert user.is_active is True
        assert user.is_superuser is True
