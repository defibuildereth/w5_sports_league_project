import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("ICTFC", "Tapestry")
        self.team2 = Team("HMFC", "Robbo")

    def test_team_has_name(self):
        self.assertEqual("ICTFC", self.team1.name)

    def test_team_has_manager(self):
        self.assertEqual("Robbo", self.team2.manager)