from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.core.profile_utils import get_profile
from my_music_app.profiles.forms import CreateProfileForm


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('home')

    context = {
    }

    return render(request, 'profile-delete.html', context)
