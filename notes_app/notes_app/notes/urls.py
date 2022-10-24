from django.urls import path

from notes_app.notes.views import home_page, profile_details, add_note, edit_note, details_note, delete_note, \
    create_profile, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('profile/', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('delete/', delete_profile, name='delete profile'),
)