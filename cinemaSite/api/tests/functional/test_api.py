import json

import pytest
import os
import django
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
class TestRestEndpoints:
    def test_movies_request(self, rest_client, user_fixture, movie_fixture):

        refresh = RefreshToken.for_user(user_fixture)
        rest_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        response = rest_client.get('/api/movies/')
        content = json.loads(response.content)
        print(content)

        assert response.status_code == 200

    def test_movies_unauthorized(self, rest_client):
        response = rest_client.get('/api/movies/')
        content = json.loads(response.content)
        print(content)

        assert response.status_code == 401

    def test_movies_by_id_request(self, rest_client, user_fixture, movie_fixture):
        refresh = RefreshToken.for_user(user_fixture)
        rest_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        response = rest_client.get(f'/api/movies/{movie_fixture.id}', follow=True)
        content = json.loads(response.content)
        print(content)

        assert response.status_code == 200

    def test_movies_by_id_unauthorized(self, rest_client):
        response = rest_client.get('/api/movies/')
        content = json.loads(response.content)
        print(content)

        assert response.status_code == 401
