from db.run_sql import run_sql
from models.team import Team
from models.game import Game

import repositories.game_repository as game_repository

def delete_all():
    # deletes all teams
    sql = "DELETE FROM teams"
    run_sql(sql)

def save(team):
    # saves team into db
    sql = "INSERT INTO teams (name, manager) VALUES (%s, %s) RETURNING *"
    values = [team.name, team.manager]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    # returns all teams in the db
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row['name'], row['manager'], row['id'])
        teams.append(team)
    return teams

def select(id):
    # returns a team object for a given team id
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        team = Team(row['name'], row['manager'], row['id'])
    return team

def teams(game_id):
    # returns all teams (team objects) who played in a given game (id)
    teams = []
    game = game_repository.select(game_id)
    teams.append(select(game.team1.id))
    teams.append(select(game.team2.id))
    return teams
    