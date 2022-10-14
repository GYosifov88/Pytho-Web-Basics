from django.shortcuts import render, redirect

from gamesplay_app.core.profile_utils import get_profile
from gamesplay_app.game.models import Game


def home_page(request):
    profile = get_profile()
    if not profile:
        return render(request, 'home-page-no-profile.html')

    return render(request, 'home-page-with-profile.html')


def show_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'dashboard.html', context)
