from django.shortcuts import render, redirect

from my_music_app.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from my_music_app.album.models import Album
from my_music_app.core.profile_utils import get_profile
from my_music_app.profiles.forms import CreateProfileForm


def home(request):
    profile = get_profile()
    albums = Album.objects.all()
    if not profile:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CreateProfileForm()

        context = {
            'form': form,
            'albums': albums,
        }

        return render(request, 'home-no-profile.html', context)
    context = {
        'albums': albums,
        'profile': profile
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'delete-album.html', context)
