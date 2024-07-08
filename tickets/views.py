from rest_framework import generics, permissions
from .models import Ticket
from .serializers import TicketSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class TicketListCreateView(generics.ListCreateAPIView):
    """
    View to list all tickets or create a new ticket.
    Only authenticated users can create tickets.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a ticket.
    Only the owner of the ticket or admin can update or delete it.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrReadOnly]
