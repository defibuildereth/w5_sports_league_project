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
game1 = Game(team1, team2, 4, 0)
game2 = Game(team2, team1, 0, 3)
game3 = Game(team1, team2, 2, 2)

league = League([team1, team2], [game1, game2, game3])

team_repository.save(team1)
team_repository.save(team2)

game_repository.save(game1)
game_repository.save(game2)
game_repository.save(game3)


pdb.set_trace()