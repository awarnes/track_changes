from django.core.management.base import BaseCommand
from tracking.models import TrackChange
from practice_accounts.models import TestUser

class Command(BaseCommand):
    """
    Command to populate the database with all information stored in CSVs for 5th Edition DnD.
    """

    # args
    help = 'Will auto populate the database with 100 test users to track that change loggin is working properly.'

    def handle(self, *args, **kwargs):

        for i in range(100):

            user = TestUser(first_name='user#{}'.format(i))
            user.save()
            user.last_name = 'y'
            user.save()
            user.email = 'x#{}@email.com'.format(i)
            user.first_name = 'User#{}'.format(i)
            user.save()
            user.delete()