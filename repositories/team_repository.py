from db.run_sql import run_sql
from models.team import Team
from models.game import Game

def delete_all():
    sql = "DELETE * FROM teams"
    run_sql(sql)


# def select_all():
#     teams = []
#     sql = "SELECT * FROM teams"
#     results = run_sql(sql)
#     for row in results:
#         team = Team(row['name'], row['manager'], row['id'])
#         teams.append(team)
#     return teams