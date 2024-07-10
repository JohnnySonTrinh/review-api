from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """
    A model for users to submit inquiries or support tickets.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tickets'
        )
    title = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'Ticket {self.id} from {self.owner.username}'
