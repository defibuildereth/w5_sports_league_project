from flask import Flask, render_template, request, redirect, Blueprint

import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
from models.game import Game

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("/games/index.html", games = games)

@games_blueprint.route("/games/new")
def new_game():
    teams = team_repository.select_all()
    scores = game_repository.random_scores()
    return render_template("/games/new.html", teams = teams, scores = scores)

@games_blueprint.route("/games", methods=["POST"])
def add_game():
    team1_id = request.form['team1']
    team1 = team_repository.select(team1_id)
    team2_id = request.form['team2']
    team2 = team_repository.select(team2_id)
    team1_goals = request.form['team1_goals']
    team2_goals = request.form['team2_goals']
    game = Game(team1, team2, team1_goals, team2_goals)
    game_repository.save(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>")
def show_game(id):
    game = game_repository.select(id)
    return render_template("/games/show.html", game = game)
