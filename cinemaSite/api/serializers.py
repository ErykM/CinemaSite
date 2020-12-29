from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Movie, Ticket


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'ticket_price', 'rating')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', )
