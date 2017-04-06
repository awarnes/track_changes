"""
Serializing the TrackChange model to be able to view it through the DRF api view.
"""

from rest_framework import serializers
from .models import TrackChange


class TrackChangeSerializer(serializers.ModelSerializer):
    """Serialize the TrackChange model."""

    class Meta:
        model = TrackChange

        fields =('operation', 'changed_fields', 'changed_data', 'changed_pk', 'changed_class', 'time_changed')