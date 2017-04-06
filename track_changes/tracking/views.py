"""
Views for DRF api to see the TrackChanges.
"""


from rest_framework import viewsets

from .models import TrackChange
from .serializers import TrackChangeSerializer


class TrackChangeViewSet(viewsets.ModelViewSet):
    """For viewing the TrackChange models."""

    queryset = TrackChange.objects.all()
    serializer_class = TrackChangeSerializer