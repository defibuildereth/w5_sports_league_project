import pdb
from models.team import Team
from models.game import Game

import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

game_repository.delete_all()
team_repository.delete_all()