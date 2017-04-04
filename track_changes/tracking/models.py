from django.db import models


class TrackChange(models.Model):
    """The table where tracked changes are stored."""

    # The different possible operations for an action (CRUD).
    OPERATIONS = (
        ('CR', 'Created'),
        ('RE', 'Retrieved'),
        ('UP', 'Updated'),
        ('DE', 'Deleted'),
    )

    operation = models.CharField(max_length=2, choices=OPERATIONS)
    changed_fields = models.CharField(max_length=1024)
    changed_data = models.CharField(max_length=1024)
    changed_pk = models.BigIntegerField()
    changed_class = models.CharField(max_length=128)
    time_changed = models.DateTimeField(auto_now_add=False)
