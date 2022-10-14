from django.shortcuts import render, redirect

from gamesplay_app.core.profile_utils import get_profile
from gamesplay_app.game.models import Game
from gamesplay_app.profiles.forms import CreateProfileForm, EditProfileForm
from gamesplay_app.profiles.models import Profile


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'details-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        Game.objects.all().delete()
        return redirect('home page')

    context = {
    }

    return render(request, 'delete-profile.html', context)


