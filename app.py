from flask import Flask, render_template

from controllers.team_controller import teams_blueprint
from controllers.game_controller import games_blueprint

app = Flask(__name__)


app.register_blueprint(games_blueprint)
app.register_blueprint(teams_blueprint)


import repositories.team_repository as team_repository

@app.route('/')
def home():
    teams = team_repository.select_all()
    return render_template('index.html', teams = teams)

if __name__ == '__main__':
    app.run(debug=True)