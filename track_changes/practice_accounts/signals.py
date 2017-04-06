"""
Signals file to ensure that each new user is given an auth token.

User in this instance will be the builtin User.
"""

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def associate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Ensure that all current accounts have AuthTokens:

for user in User.objects.all():

    if user != Token.objects.filter(user=user)[0]:
        Token.objects.get_or_create(user=user)
