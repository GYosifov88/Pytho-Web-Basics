from django.shortcuts import render, redirect

from gamesplay_app.game.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.game.models import Game


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateGameForm()

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditGameForm(instance=game)

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):

    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('home')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'game': game,
        'form': form,
    }

    return render(request, 'delete-game.html', context)

