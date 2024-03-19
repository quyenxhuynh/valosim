from constants import Map, Status
from team import Team
import logging
import uuid


class Game:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.id = uuid.uuid4()

        self.map: Map = Map.NONE
        self.status: Status = Status.NOT_STARTED

        self.alpha: Team = None
        self.alpha_score: int = 0

        self.omega: Team = None
        self.omega_score: int = 0

        self.winner = None
        self.loser = None

    def update_game_status(self) -> None:
        if self.status == Status.COMPLETE:
            return

        if self.alpha_score == 0 and self.omega_score == 0:
            self.status = Status.NOT_STARTED
            return

        if self.alpha_score >= 13 or self.omega_score >= 13:
            if abs(self.alpha_score - self.omega_score) >= 2:
                self.status = Status.COMPLETE
                self.update_teams()
                return

        self.status = Status.IN_PROGRESS

    def update_teams(self) -> None:
        if self.status == Status.COMPLETE:
            if self.alpha_score > self.omega_score:
                self.winner = self.alpha
                self.loser = self.omega
            else:
                self.winner = self.omega
                self.loser = self.alpha

    def update_score(self, alpha_score: int, omega_score: int, force: bool = False) -> None:
        if self.status == Status.COMPLETE and not force:
            self.logger.info(f"The game was marked complete. Scores will not be updated.")
            return

        self.update_game_status()
        self.alpha_score = alpha_score
        self.omega_score = omega_score

    def get_game_status(self) -> Status:
        return self.status

    def get_winner(self) -> Team:
        return self.winner

    def get_loser(self) -> Team:
        return self.loser

    def __str__(self):
        return f"{self.alpha} {self.alpha_score}-{self.omega_score} {self.loser}"
