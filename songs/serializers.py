from .models import Song
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Song
        # the fields that should be included in the serialized output
        fields = ['id', 'title', 'artist']