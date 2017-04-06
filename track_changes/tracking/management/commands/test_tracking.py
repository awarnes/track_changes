from django.core.management.base import BaseCommand
from tracking.models import TrackChange
from practice_accounts.models import TestUser
from organizations.models import Organization

class Command(BaseCommand):
    """
    Command to test model change tracking with 50 iterations of creation, updating, and deletion.
    """

    # args
    help = 'Will test with 50 iterations of a flow of creating, updating, and deleting models to ensure that change logging is working properly.'

    def handle(self, *args, **kwargs):

        for i in range(50):

            user = TestUser(first_name='user#{}'.format(i))
            user.save()
            user.last_name = 'y'
            user.save()
            user.email = 'x#{}@email.com'.format(i)
            user.first_name = 'User#{}'.format(i)
            user.save()
            org = Organization(name='A', slug='a#{}'.format(i))
            org.save()
            org.name = 'B'
            org.save()
            user.delete()
            org.delete()
