from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review

class Rating(models.Model):
    """
    Rating model, related to 'owner' and 'review'.
    'owner' is a User instance and 'review' is a review instance.
    'stars' is an integer field with choices from 1 to 5.
    'unique_together' ensures a user can't rate the same review twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name='ratings', on_delete=models.CASCADE
    )
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'review']

    def __str__(self):
        return f'{self.owner} rated {self.review} - {self.stars} stars'
