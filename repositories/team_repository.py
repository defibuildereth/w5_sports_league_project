from db.run_sql import run_sql
from models.team import Team
from models.game import Game

import repositories.game_repository as game_repository

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def save(team):
    sql = "INSERT INTO teams (name, manager) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.manager]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row['name'], row['manager'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        team = Team(row['name'], row['manager'], row['id'])
    return team

def teams(game_id):
    teams = []
    game = game_repository.select(game_id)
    teams.append(select(game.team1.id))
    teams.append(select(game.team2.id))
    return teams
    