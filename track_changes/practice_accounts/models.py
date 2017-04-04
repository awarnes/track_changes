from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
# class User(AbstractUser):
#     """Base user class for the application, should further abstraction be necessary. (Not currently added as base user model.)"""
#

class TestUser(models.Model):
    """Test model for ensuring that user information can be tracked as it's changed."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

