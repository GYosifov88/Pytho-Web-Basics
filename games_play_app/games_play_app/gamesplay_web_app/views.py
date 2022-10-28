from django.shortcuts import render, redirect

from games_play_app.core.profile_utils import get_profile
from games_play_app.gamesplay_web_app.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, \
    EditProfileForm, DeleteProfileForm
from games_play_app.gamesplay_web_app.models import Game


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def dashboard_page(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def profile_create(request):
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


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)


def game_create(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
        'profile': profile,
        'game': game,
    }

    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'delete-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
        'profile': profile
    }

    return render(request, 'details-game.html', context)
