import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

class League():
    def __init__(self, teams = [], games = []):
        self.teams = teams
        self.games = games

    def get_teams(self):
        teams = team_repository.select_all()
        return teams

    def get_games(self):
        games = game_repository.select_all()
        return games

    def get_games_played(self, id):
        return len(game_repository.games(id))


    # def full_league():
    #     league_dict = {}
