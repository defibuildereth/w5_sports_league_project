import repositories.team_repository as team_repository
import repositories.game_repository as game_repository
from models.team import Team


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
        points = 0
        game = game_repository.select(game_id)
        if game.team1_goals == game.team2_goals:
            points = 1
        elif game.team1.id == team_id:
            if game.team1_goals > game.team2_goals:
                points = 3
        elif game.team2.id == team_id:
            if game.team2_goals > game.team1_goals:
                points = 3
        else:
            points = 0
        return points

    def get_total_points(self, team_id):
        total_points = 0
        relevant_games = game_repository.games(team_id)
        for game in relevant_games:
            total_points += self.get_game_points(game.id, team_id)
        return total_points


    def full_league(self):
        league_dict = {}
        teams = team_repository.select_all()
        for team in teams:
            league_dict[team.name] = [self.get_games_played(team.id), self.get_total_points(team.id)]

        sorted_dict = dict(sorted(league_dict.items(), key=lambda item: item[1][1], reverse = True))

        return sorted_dict

    # def order_teams(self):

    #     teams_in_order = []
    #     league = self.full_league() # returns a dictionary
    #     index = 0

        # for team in league:
        #     if len(teams_in_order) == 0:
        #         team_object = team_repository.select_name(team)
        #         teams_in_order.append(team_object)

        
        # while index < len(league):
        #     if league[team][1] > teams_in_order[index]:
        #         teams_in_order.insert(index, team)
        #     else:
        #         index += 1
        # teams_in_order.append(team)

        # return teams_in_order