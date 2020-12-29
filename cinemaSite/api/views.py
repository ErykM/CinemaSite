from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer, TicketSerializer
from .models import Movie, Ticket


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
