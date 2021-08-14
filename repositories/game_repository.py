from db.run_sql import run_sql
from models.team import Team
from models.game import Game

def delete_all():
    sql = "DELETE * FROM games"
    run_sql(sql)