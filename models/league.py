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

    def get_games_played(self, team_id):
        return len(game_repository.games(team_id))

    def get_game_points(self, game_id, team_id):
        
        game = game_repository.select(game_id)
        if game.team1_goals == game.team2_goals:
            points = 1
        elif game.team1.id == team_id:
            if game.team1_goals > game.team2_goals:
                points = 3
        else:
            points = 0
        return points



    # def full_league():
    #     league_dict = {}
