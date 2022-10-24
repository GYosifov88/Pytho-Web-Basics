from notes_app.notes.models import Profile, Note


def get_profile():
    profile = Profile.objects.first()
    if profile:
        profile.notes = Note.objects.all()
        profile.notes_count = profile.notes.count()
    return profile
