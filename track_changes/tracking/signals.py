"""
Signal for updating the TrackChange model from all information on other possible models.
"""

# Signal Imports:
from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete, m2m_changed)
from django.core.signals import (request_started, request_finished, got_request_exception)

# Django Imports:
from django.dispatch import receiver

@receiver([pre_save, post_save])
def track_save(sender, instance, **kwargs):
    """Tracks the save signals for models in or out of the Django Admin."""

    print("Sender: {}".format(sender))
    print("Instance: {}".format(instance))
    for kword, kwarg_value in kwargs.items():
        print("{}: {}".format(kword, kwarg_value))
