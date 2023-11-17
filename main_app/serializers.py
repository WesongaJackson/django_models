from rest_framework import serializers

from main_app.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'phone', 'id']


class AlbumSerializer(serializers.ModelSerializer):
    artists=serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ['name','release_year', 'id','artists']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album', 'id']


class ArtistAlbumSerializer(serializers.ModelSerializer):

    # albums = serializers.StringRelatedField(read_only=True, many=True)
    albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Artist
        fields = ['name', 'phone', 'albums']
# TODO elastic search,celery,redis cache
