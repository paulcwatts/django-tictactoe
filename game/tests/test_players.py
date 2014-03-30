import random
from django.test import TestCase

from game.models import Game
from game.players import get_player, RandomPlayer


class RandomPlayerTest(TestCase):
    def test_import(self):
        p = get_player("game.players.RandomPlayer")
        self.assertEqual(type(p), RandomPlayer)

    def test_random(self):
        """
        Basic testing.
        """
        random.seed(0)  # For testing
        game = Game()
        p1 = RandomPlayer()

        game.play(p1.play(game))
        self.assertEqual(game.board, "       X ")

    def test_play_to_end(self):
        """
        Play two random players against each other.
        """
        random.seed(0)  # For testing
        game = Game()
        p1 = RandomPlayer()
        p2 = RandomPlayer()

        while not game.is_game_over:
            game.play(p1.play(game))
            # Check to see if the 1st player one
            if game.is_game_over:
                break
            game.play(p2.play(game))

        self.assertEqual(game.board, "OOXOX OXX")
        self.assertEqual(game.is_game_over, 'O')
