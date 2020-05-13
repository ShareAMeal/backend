from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class AssoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Association
        exclude = ['admin']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        exclude = ['organizer']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['password']
