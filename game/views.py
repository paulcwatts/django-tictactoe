from django.shortcuts import render, get_object_or_404

from .models import Game


def index(request):
    return render(request, "game/game_list.html")


def game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, "game/game_detail.html", {
        'game': game
    })
