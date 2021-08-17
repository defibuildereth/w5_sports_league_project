import pdb
from models.team import Team
from models.game import Game
from models.league import League

import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

game_repository.delete_all()
team_repository.delete_all()

team1 = Team("ICTFC", "Tapestry")
team2 = Team("HMFC", "Robbo")
game = Game(team1, team2, 4, 0)
league = League([team1, team2], [game])

team_repository.save(team1)
team_repository.save(team2)

game_repository.save(game)

pdb.set_trace()