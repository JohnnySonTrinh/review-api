from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Review(models.Model):
    """
    Model for a review post. stores the title, content, github repo, 
    live website, image, created_on, updated_on.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(max_length=1000, blank=True)
    github_repo = models.URLField(
        blank=True,
        max_length=255,
    )
    live_website = models.URLField(
        blank=True,
        max_length=255,
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_xw5she'
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.id} - {self.title}'