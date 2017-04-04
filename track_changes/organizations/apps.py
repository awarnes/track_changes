from django.apps import AppConfig

from django.db.models.signals import (pre_save, post_save)


class OrganizationsConfig(AppConfig):
    name = 'organizations'

    def ready(self):
        """Ensure the signals to catch changes and save to TrackChange model."""

        import tracking.signals