import unittest
from models.game import Game
from models.team import Team

class TestGame(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("ICTFC", "Tapestry")
        self.team2 = Team("HMFC", "Robbo")
        self.game = Game(self.team1, self.team2, 4, 0)

    def test_game_has_team1(self):
        self.assertEqual("ICTFC", self.game.team1.name)
