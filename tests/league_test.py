import unittest
from models.game import Game
from models.team import Team
from models.league import League

import repositories.team_repository as team_repository

class TestLeague(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("ICTFC", "Tapestry")
        self.team2 = Team("HMFC", "Robbo")
        self.game = Game(self.team1, self.team2, 4, 0)
        self.league = League([self.team1, self.team2], self.game)

    def test_league_has_teams(self):
        self.assertEqual(2, len(self.teams))