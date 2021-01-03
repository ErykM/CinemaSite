import json

import pytest
import os
import django


@pytest.mark.django_db
class TestRestEndpoints:
    def test_movies_request(self, rest_client):
        response = rest_client.get('/api/movies/')
        content = json.loads(response.content)
        print(content)
        assert response.status_code == 202
