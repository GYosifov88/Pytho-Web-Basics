from gamesplay_app.game.models import Game
from gamesplay_app.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()

    return profile
