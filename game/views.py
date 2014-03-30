from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewGameForm
from .models import Game


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        # Theoretically the only way this form can be invalid
        # is in the case of progammer error or malfeasance --
        # the user doesn't have anything to do.
        if form.is_valid():
            game = form.create()
            # In case the computer is X, it goes first.
            game.play_auto()
            return redirect(game)
    else:
        form = NewGameForm()
    return render(request, 'game/game_list.html', {'form': form})


def game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "game/game_detail.html", {
        'game': game
    })
