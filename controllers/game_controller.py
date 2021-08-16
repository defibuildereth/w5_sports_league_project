from flask import Flask, render_template, request, redirect, Blueprint

import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("/games/index.html", games = games)

@games_blueprint.route("/games/new")
def new_game():
    teams = team_repository.select_all()
    return render_template("/games/new.html", teams = teams)