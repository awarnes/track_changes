from django.db import models


class TestUser(models.Model):
    """Test model for ensuring that user information can be tracked as it's changed."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return '{0.first_name} {0.last_name}'.format(self)