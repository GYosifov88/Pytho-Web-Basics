from online_library.books.models import Book
from online_library.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        profile.books = Book.objects.all()
        profile.books_count = profile.books.count()
    return profile
