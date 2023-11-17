from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.models import Artist, Song
from main_app.serializers import ArtistSerializer, ArtistAlbumSerializer


# Create your views here.
def show(request):
    # artist=Artist.objects.order_by('?').first()
    # print(artist)
    # albums=artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #     print(alb.name,alb.release_year)
    #     songs=alb.songs.all()
    #     print(len(songs),"songs")
    #     for s in songs:
    #         print("song  -" ,s.title,s.duration,"seconds")
    song = Song.objects.order_by("?").first()
    print(song)
    album = song.album
    print(album)
    # artist=song.album.artists.all().values("name")
    # print(artist)
    artist = song.album.artists.all().values("name")

    return HttpResponse(artist)


@api_view(["GET", "POST"])
def save_or_fetch_artists(request):
    if request.method == "GET":
        artist = Artist.objects.all()
        serializer = ArtistSerializer(instance=artist, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message": "added artist", "data": serializer.data})


@api_view(["GET"])
def fetch_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["PUT", "PATCH"])
def update_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


@api_view(["DELETE"])
def delete_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        artist.delete()

        return Response({"message":"successfully deleted"})
    except:
        return Response({"error": "Artist not found"}, status=404)

@api_view(["GET"])
def albums_for_artist(request,id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistAlbumSerializer(instance=artist)


        return Response(serializer.data)
    except:
        return Response({"error": "Artist not found"}, status=404)


