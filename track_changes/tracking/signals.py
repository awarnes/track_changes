"""
Signals for creating instances of the TrackChange model from all information on other possible models.
"""
# Python Imports:
import json

# Track Changes:
from .models import TrackChange

# Signal Imports:
from django.db.models.signals import (post_save, pre_delete)

# Django Imports:
from django.dispatch import receiver
from django.db.models import Q
from django.contrib.admin.models import LogEntry


# Do not specify sender to automatically receive the signal for every model.
@receiver(post_save)
def track_create_and_update(sender, instance, **kwargs):

    # Since not filtering models, need to filter out the TrackChange, and LogEntry model since we do not need to track them.
    if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):


        tracked_change = TrackChange.objects.create(
            operation='CR' if kwargs.get('created') else 'UP',

            changed_data=json.dumps({"{}".format(field.attname): getattr(instance, str(field.name)) for field in instance._meta.get_fields()\
                          if field.attname not in ('id') and getattr(instance, str(field.name)) != ''}),

            changed_pk=instance.pk,
            changed_class=sender.__name__,
        )

        if not kwargs.get('created'):
            previous_state = TrackChange.objects.filter(Q(changed_pk=instance.pk), Q(changed_class=sender.__name__)).latest(field_name='time_changed')

            changed_fields = [field.name for field in instance._meta.get_fields()
                              if json.loads(previous_state.changed_data).get(str(field.name)) != getattr(instance, str(field.name))
                              and field.name not in ('id')]
        else:
            changed_fields = [field_name for field_name, field_value in json.loads(tracked_change.changed_data).items()
                              if field_value != '']

        tracked_change.changed_fields = changed_fields
        tracked_change.save()

@receiver(pre_delete)
def track_delete(sender, instance, using, **kwargs):
    """To track any deleted object, except for tracking objects themselves and LogEntries."""

    if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):

        TrackChange.objects.create(
            operation='DE',
            changed_fields='None',
            changed_data='None',
            changed_pk=instance.pk,
            changed_class=sender.__name__,
        )