"""
Signals for creating instances of the TrackChange model from all information on other possible models.

Using signals we are able to get information whenever a model is saved (including create and update actions) or deleted.
By using these signals we can hijack the process to get information about what is being saved or deleted and create a
change record that is then saved separately into the database.

Without a sender model being designated in the receiver decorator it will be attached to every model in the database.
If change tracking is only needed for certain models, the sender can be designated as such:

    @receiver(post_save, sender=TestUser)
                or
    senders = (TestUser, Organization)
    @receiver(post_save. sender=senders
"""
# Python Imports:
import json

# Track Changes:
from .models import TrackChange
from practice_accounts.models import TestUser
from organizations.models import Organization

# Signal Imports:
from django.db.models.signals import (post_save, pre_delete)

# Django Imports:
from django.dispatch import receiver
from django.db.models import Q
from django.contrib.admin.models import LogEntry

# Specify which models need to be tracked, and add sender=senders to each receiver if not tracking the whole database.
# senders = (TestUser,)


# Do not specify sender in order to automatically receive the signal for every model in the project.
@receiver(post_save,)
def track_create_and_update(sender, instance, **kwargs):

    # Since not filtering models, need to filter out the TrackChange, and LogEntry model since we do not need to track them.
    if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):

        # Create a new instance to store the tracked changes:
        tracked_change = TrackChange.objects.create(
            operation='CR' if kwargs.get('created') else 'UP',

            changed_data=json.dumps({"{}".format(field.attname): getattr(instance, str(field.name)) for field in instance._meta.get_fields()\
                          if field.attname not in ('id',) and getattr(instance, str(field.name)) != ''}),

            changed_pk=instance.pk,
            changed_class=sender.__name__,
        )

        # Use previous state data to determine which fields have changed between the two instances.
        if not kwargs.get('created'):
            previous_state = TrackChange.objects.filter(Q(changed_pk=instance.pk), Q(changed_class=sender.__name__))\
                                                .order_by('-time_changed')[1]

            # import pdb; pdb.set_trace()
            changed_fields = [field_name for field_name, field_value in json.loads(tracked_change.changed_data).items()
                              if field_value != json.loads(previous_state.changed_data).get(field_name)]
        else:
            changed_fields = [field_name for field_name, field_value in json.loads(tracked_change.changed_data).items()
                              if field_value != '']

        tracked_change.changed_fields = changed_fields
        tracked_change.save()


# Do not specify sender in order to automatically receive the signal for every model in the project.
@receiver(pre_delete,)
def track_delete(sender, instance, using, **kwargs):
    """To track any deleted object, except for tracking objects themselves and LogEntries."""

    # Since not filtering models, need to filter out the TrackChange, and LogEntry model since we do not need to track them.
    if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):

        TrackChange.objects.create(
            operation='DE',
            changed_fields='None',
            changed_data='None',
            changed_pk=instance.pk,
            changed_class=sender.__name__,
        )