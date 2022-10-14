from django.urls import path

from gamesplay_app.game.views import create_game, edit_game, delete_game, game_details

urlpatterns = (
    path('create/', create_game, name='create game'),
    path('details/<int:id>', game_details, name='game details'),
    path('edit/<int:id>', edit_game, name='edit game'),
    path('delete/<int:id>', delete_game, name='delete game')
)