from game import Game


class Match:
    def __init__(self):
        self.games: list[Game] = []
        self.winner = None
        self.loser = None

    def get_winner(self):
        return self.winner

    def get_loser(self):
        return self.loser
