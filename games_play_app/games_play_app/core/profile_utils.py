from games_play_app.gamesplay_web_app.models import Profile, Game


def get_profile():
    profile = Profile.objects.first()
    if profile:
        profile.games = Game.objects.all()
        profile.games_count = profile.games.count()
        if profile.first_name and profile.last_name:
            profile.full_name = f"{profile.first_name} {profile.last_name}"
        elif profile.first_name and not profile.last_name:
            profile.full_name = f"{profile.first_name}"
        elif profile.last_name and not profile.first_name:
            profile.full_name = f"{profile.last_name}"
        if profile.games:
            profile.avg_rating = sum(g.rating for g in profile.games) / profile.games_count
    return profile
