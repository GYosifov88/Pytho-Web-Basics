from django.urls import path

from gamesplay_app.profiles.views import create_profile, edit_profile, delete_profile, profile_details

urlpatterns = (
    path('create/', create_profile, name='create profile'),
    path('details/', profile_details, name='profile details'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
)