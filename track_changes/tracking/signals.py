"""
Signal for updating the TrackChange model from all information on other possible models.
"""
# Python Imports:
from datetime import datetime as dt

# Track Changes:
from .models import TrackChange

# Signal Imports:
from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete, m2m_changed)
from django.core.signals import (request_started, request_finished, got_request_exception)

# Django Imports:
from django.dispatch import receiver

@receiver([pre_save, post_save])
def track_save(sender, instance, **kwargs):
    """Tracks the save signals for models in or out of the Django Admin."""

    if not isinstance(instance, TrackChange):

        TrackChange.objects.create(
            operation='CR',
            changed_fields='name',
            changed_data='42',
            changed_pk=5,
            # changed_class='sender',
            time_changed=dt.now()
        )