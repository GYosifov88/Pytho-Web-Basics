from my_music_app.album.models import Album
from my_music_app.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        profile.albums = Album.objects.all()
        profile.album_count = profile.albums.count()
    return profile
