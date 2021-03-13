from rest_framework import serializers
from music.models import Playlist, Music, Track, CurrentSong

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentSong
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('__all__',)