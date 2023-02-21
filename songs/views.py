from django.shortcuts import render
from .models import Song
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SongSerializer

# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Song.objects.all()
    # The serializer class for serializing output
    serializer_class = SongSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]