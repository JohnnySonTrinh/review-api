# tickets/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    """
    List all tickets or create a new ticket.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a ticket instance.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'resolved' in request.data:
            instance.resolved = request.data['resolved']
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super().patch(request, *args, **kwargs)
