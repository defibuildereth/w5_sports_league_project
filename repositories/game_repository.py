from pdb import run
from db.run_sql import run_sql
from models.team import Team
from models.game import Game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

# def select_all():
#     games = []
#     sql = "SELECT * FROM games"
#     results = run_sql(sql)
#     for row in results:
#         game = Game()

def save(game):
    sql = "INSERT INTO games (team_1, team_2, team_1_goals, team_2_goals) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [game.team1.id, game.team2.id, game.team1_goals, game.team2_goals]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game