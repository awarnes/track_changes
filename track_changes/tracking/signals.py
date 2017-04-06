"""
Signal for updating the TrackChange model from all information on other possible models.
"""
# Python Imports:
import json

# Track Changes:
from django.contrib.admin.models import LogEntry
from django.forms.models import model_to_dict
from .models import TrackChange

# Signal Imports:
from django.db.models.signals import (pre_save, pre_init, post_save, pre_delete, post_delete, m2m_changed)
from django.core.signals import (request_started, request_finished, got_request_exception)

# Django Imports:
from django.dispatch import receiver
from django.db.models import Q


# def check_for_changed_fields(prev_model_instance, new_model_instance):
#     """Helper function to check if a model's fields have changed."""
#
#     changed_fields = {field.name: getattr(new_model_instance, field.name) for field in new_model_instance._meta.get_fields() if getattr(new_model_instance, field) != getattr(prev_model_instance, field)}
#
# @receiver(pre_save)
# def track_updated(sender, instance, **kwargs):
#     """Tracks the save signals for models in or out of the Django Admin."""
#
#     # instance
#
#     if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):
#         tracked_change = TrackChange.objects.create(
#             operation='UP',
#             changed_fields=kwargs.get('update_fields') or 'None',
#             changed_data='42',
#             changed_pk=instance.pk or 0,
#             changed_class=sender.__dict__,
#         )


@receiver(post_save)
def track_create_and_update(sender, instance, **kwargs):

    if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):

        if not kwargs.get('created'):
            previous_state = TrackChange.objects.filter(Q(changed_pk=instance.pk), Q(changed_class=sender.__name__)).latest(field_name='time_changed')

            changed_fields = [field.name for field in instance._meta.get_fields()
                              if json.loads(previous_state.changed_data).get(str(field.name)) != getattr(instance, str(field.name))
                              and field.name not in ('id')]

        TrackChange.objects.create(
            operation='CR' if kwargs.get('created') else 'UP',

            changed_fields=changed_fields,

            changed_data=json.dumps({"{}".format(field.attname): getattr(instance, str(field.name)) for field in instance._meta.get_fields()\
                          if field.attname not in ('id') and getattr(instance, str(field.name)) != ''}),
            changed_pk=instance.pk,

            changed_class=sender.__name__,
        )

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