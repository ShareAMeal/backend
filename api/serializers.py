from rest_framework import serializers

from . import models


class AssoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assocation
        exclude = []  # ['admin']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        exclude = ['organizer']