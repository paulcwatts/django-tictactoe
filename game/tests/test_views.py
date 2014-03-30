import random

from django.core.urlresolvers import reverse
from django.test import TestCase

from game.models import Game


class ViewsTest(TestCase):
    def test_index_redirect(self):
        "Tests the redirection from the index URL"

        response = self.client.get(reverse('index'))
        self.assertRedirects(response, reverse('game:index'), status_code=301)

    def test_index(self):
        "Views the game index page. Not much here right now."

        response = self.client.get(reverse('game:index'))
        self.assertTemplateUsed(response, 'game/game_list.html')

    def test_index_post(self):
        "Posting to the index view gives you a new game."
        random.seed(0)

        response = self.client.post(reverse('game:index'), {
            'player1': 'human',
            'player2': 'game.players.RandomPlayer'
        })
        self.assertEqual(Game.objects.count(), 1)
        game = Game.objects.all()[0]
        self.assertRedirects(response, game.get_absolute_url())
        self.assertEqual(game.board, "         ")

        # Players are assigned.
        self.assertEqual(game.player_x, 'human')
        self.assertEqual(game.player_o, 'game.players.RandomPlayer')

    def test_detail(self):
        "Views the game detail page."

        game = Game.objects.create()
        response = self.client.get(game.get_absolute_url())
        self.assertTemplateUsed(response, 'game/game_detail.html')
