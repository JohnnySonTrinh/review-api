import random
from django.core.management.base import BaseCommand
from profiles.models import Profile

class Command(BaseCommand):
    help = 'Update all profile images to a random default image'

    # List of default images
    DEFAULT_IMAGES = [
        '../default_profile_h8s2sm.webp',
        '../default_profile_kxm3io.webp',
        '../default_profile_xw5shd.webp',
        # Add more paths to default images as needed
    ]

    def handle(self, *args, **kwargs):
        profiles = Profile.objects.all()
        for profile in profiles:
            profile.image = random.choice(self.DEFAULT_IMAGES)
            profile.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated all profile images'))

