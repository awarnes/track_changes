from django.apps import AppConfig


class PracticeAccountsConfig(AppConfig):
    name = 'practice_accounts'

    def ready(self):
        """Ensure the signals to catch changes and save to TrackChange model."""

        import practice_accounts.signals