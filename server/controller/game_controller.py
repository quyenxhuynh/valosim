from models.game import Game
from models.team import Team
from constants import Map


def create_game(team1: Team, team2: Team, team1_score: int = 0, team2_score: int = 0, map: Map = Map.NONE):
    game = Game()
    game.alpha = team1
    game.omega = team2
    game.map = map
    game.update_score(team1_score, team2_score)
    return game


def get_game(uuid: str):
    pass
