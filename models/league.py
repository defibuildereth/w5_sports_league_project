import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

class League():
    def __init__(self, teams = None, games = None):
        self.teams = teams
        self.games = games

    def get_teams():
        teams = team_repository.select_all()
        return teams

    def get_games():
        games = game_repository.select_all()
        return games

    def get_games_played(team):
        return len(team_repository.games(team.id))


    # def full_league():
    #     league_dict = {}
