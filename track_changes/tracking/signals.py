"""
Signal for updating the TrackChange model from all information on other possible models.
"""
# Python Imports:
from datetime import datetime as dt

# Track Changes:
from django.contrib.admin.models import LogEntry
from .models import TrackChange

# Signal Imports:
from django.db.models.signals import (pre_save, pre_init, post_save, pre_delete, post_delete, m2m_changed)
from django.core.signals import (request_started, request_finished, got_request_exception)

# Django Imports:
from django.dispatch import receiver


# def check_for_changed_fields(prev_model_instance, new_model_instance):
#     """Helper function to check if a model's fields have changed."""
#
#     changed_fields = {field.name: getattr(new_model_instance, field.name) for field in new_model_instance._meta.get_fields() if getattr(new_model_instance, field) != getattr(prev_model_instance, field)}
#
# @receiver(pre_save)
# def track_pre_save(sender, instance, **kwargs):
#     """Tracks the save signals for models in or out of the Django Admin."""
#
#     if not isinstance(instance, TrackChange) and not isinstance(instance, LogEntry):
#         tracked_change = TrackChange.objects.create(
#             operation='CR',
#             changed_fields=kwargs['update_fields'] or 'None',
#             changed_data='42',
#             changed_pk=instance.pk or 0,
#             changed_class=sender.__name__,
#         )
#
#         if tracked_change.changed_fields == 'None':
#             tracked_change.changed_fields = instance.objects.
#


@receiver(pre_init, sender='organizations.Organization')
def track_create(sender, **kwargs):

    if not isinstance(sender, TrackChange) and not isinstance(sender, LogEntry):

        TrackChange.objects.create(
            operation='CR',
            changed_fields=list(kwargs.keys()),
            changed_data=dict(kwargs.items()),
            changed_pk=0,
            changed_class=sender.__name__,

        )