from django.apps import AppConfig


class TrackingConfig(AppConfig):
    name = 'tracking'

    def ready(self):
        """Ensure the signals to catch changes and save to TrackChange model."""

        import tracking.signals