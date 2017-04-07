from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Command(BaseCommand):
    """
    Command to test model change tracking with 50 iterations of creation, updating, and deletion.
    """

    # args
    help = 'Run command to ensure that all users have an auth token for DRF.'

    def handle(self, *args, **kwargs):

        for user in User.objects.all():
            Token.objects.create(user=user)
