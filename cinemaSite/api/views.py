from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from .serializers import MovieSerializer, TicketSerializer, MovieByIdSerializer
from .models import Movie, Ticket


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MovieByIdSerializer
        return MovieSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        payload = request.auth.payload
        user_id = payload.get('user_id')

        queryset = Ticket.objects.filter(user__id=user_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
