from rest_framework import serializers

from .models import Movie, Ticket


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'ticket_price')


class MovieByIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'ticket_price', 'rating')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    movie_title = serializers.CharField(source='movie.title')

    class Meta:
        model = Ticket
        fields = ('id', 'movie_title')
