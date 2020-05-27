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
