import pytest
from django.test import Client
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Movie, Ticket
from users.models import CustomUser


def get_token():
    return 'token'


@pytest.fixture
def user_fixture():
    user = CustomUser.objects.create_user(name='test', email='test@user.com', password='test_password')

    return user


@pytest.fixture
def rest_client():
    client = APIClient()

    # refresh = RefreshToken.for_user(user_fixture)
    # client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client


@pytest.fixture
def movie_fixture():
    movie = Movie.objects.create(title='Shawshank Redemption', description='Really nice movie', ticket_price=10.0,
                                 rating=9.1)

    return movie


@pytest.fixture
def user_with_ticket_fixture(movie_fixture):
    user = CustomUser.objects.create_user(name='user', email='user@user.com', password='test_password')

    ticket_one = Ticket.objects.create(movie=movie_fixture, user=user)

    return user
