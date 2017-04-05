from django.db import models

# Create your models here.

class Organization(models.Model):
    """Basic organization users would be able to associate with."""

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name