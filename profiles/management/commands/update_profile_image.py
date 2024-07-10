import random
from django.core.management.base import BaseCommand
from profiles.models import Profile


class Command(BaseCommand):
    help = 'Update a profile image to a random default image'

    # List of default images
    DEFAULT_IMAGES = [
        # '../default_profile_h8s2sm.webp',
        # '../default_profile_kxm3io.webp',
        '../default_profile_xw5shd.webp',
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            'username', type=str,
            help=(
                'The username of the user whose profile image '
                'needs to be updated'
            )
        )

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            profile = Profile.objects.get(owner__username=username)
            profile.image = random.choice(self.DEFAULT_IMAGES)
            profile.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully updated profile image for user {username}'
                )
            )
        except Profile.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(
                    f'Profile for user {username} does not exist'
                )
            )
