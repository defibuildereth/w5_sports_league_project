from pdb import run
from db.run_sql import run_sql
from models.team import Team
from models.game import Game

import repositories.team_repository as team_repository

def delete_all():
    # deletes all games from db
    sql = "DELETE FROM games"
    run_sql(sql)

def select_all():
    # returns all games from db
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        team1 = team_repository.select(row['team_1'])
        team2 = team_repository.select(row['team_2'])
        game = Game(team1, team2, row['team_1_goals'], row['team_2_goals'], row['id'])
        games.append(game)
    return games

def save(game):
    # saves game into db
    sql = "INSERT INTO games (team_1, team_2, team_1_goals, team_2_goals) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [game.team1.id, game.team2.id, game.team1_goals, game.team2_goals]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

def select(id):
    # returns a game object for a given id
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        team1 = team_repository.select(row['team_1'])
        team2 = team_repository.select(row['team_2'])
        game = Game(team1, team2, row['team_1_goals'], row['team_2_goals'])
    return game

def games(team_id):
    # returns a list of game objects for a given team id
    games = []
    sql = "SELECT id FROM games WHERE team_1 = %s OR team_2 = %s"
    values = [team_id, team_id]
    results = run_sql(sql, values)

    for row in results:
        game = select(row['id'])
        games.append(game)
    
    return games