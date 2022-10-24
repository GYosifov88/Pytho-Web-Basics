from django.urls import path

from my_music_app.album.views import home, delete_album, edit_album, add_album, album_details

urlpatterns = (
    path('', home, name='home'),
    path('add/', add_album, name='add album'),
    path('details/<int:pk>/', album_details, name='album details'),
    path('edit/<int:pk>/', edit_album, name='edit album'),
    path('delete/<int:pk>/', delete_album, name='delete album'),
)