from django import forms

from gamesplay_app.game.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class CreateGameForm(GameForm):
    pass


class EditGameForm(GameForm):
    pass


class DeleteGameForm(GameForm):
    pass
