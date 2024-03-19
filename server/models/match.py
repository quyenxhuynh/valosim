from game import Game
from team import Team
from constants import BestOf


class Match:
    def __init__(self):
        self.games: list[Game] = []
        self.bo = BestOf.NONE

        self.alpha: Team = None
        self.omega: Team = None

        self.winner = None
        self.loser = None

    def update(self, game):
        pass

    def get_winner(self):
        return self.winner

    def get_loser(self):
        return self.loser
