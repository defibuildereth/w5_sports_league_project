from flask import Flask, render_template, request, redirect, Blueprint

from models.team import Team

import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("/teams/new.html")

@teams_blueprint.route("/teams", methods=["POST"])
def add_team():
    team_name = request.form['team_name']
    manager_name = request.form['manager_name']
    team = Team(team_name, manager_name)
    team_repository.save(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    team = team_repository.select(id)
    games = game_repository.games(id)
    return render_template("/teams/show.html", team = team, games = games)

@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/edit")
def update_team_form(id):
    team = team_repository.select(id)
    return render_template("teams/update.html", team = team)



