from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ticket
        fields = [
            'id',
            'owner',
            'title',
            'message',
            'email',
            'created_on',
            'resolved'
        ]
