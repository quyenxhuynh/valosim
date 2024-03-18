# RUN FROM MODELS/ DIRECTORY
import unittest
from models.game import Game
from constants import Status


class TestGameStatus(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_not_started(self):
        self.game.alpha_score = 0
        self.game.omega_score = 0
        self.game.update_game_status()
        expected = Status.NOT_STARTED
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_in_progress(self):
        self.game.alpha_score = 1
        self.game.omega_score = 0
        self.game.update_game_status()
        expected = Status.IN_PROGRESS
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_in_progress_overtime(self):
        self.game.alpha_score = 14
        self.game.omega_score = 13
        self.game.update_game_status()
        expected = Status.IN_PROGRESS
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_complete_base(self):
        self.game.alpha_score = 13
        self.game.omega_score = 5
        self.game.update_game_status()
        expected = Status.COMPLETE
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_complete_close(self):
        self.game.alpha_score = 13
        self.game.omega_score = 11
        self.game.update_game_status()
        expected = Status.COMPLETE
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_complete_flipped(self):
        self.game.alpha_score = 11
        self.game.omega_score = 13
        self.game.update_game_status()
        expected = Status.COMPLETE
        actual = self.game.status
        self.assertEqual(expected, actual)

    def test_complete_overtime(self):
        self.game.alpha_score = 21
        self.game.omega_score = 19
        self.game.update_game_status()
        expected = Status.COMPLETE
        actual = self.game.status
        self.assertEqual(expected, actual)


class TestUpdateTeamWL(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_alpha_win(self):
        self.game.status = Status.COMPLETE
        self.game.alpha_score = 13
        self.game.omega_score = 11
        self.game.update_teams()

        expected_winner = self.game.alpha
        actual_winner = self.game.winner
        self.assertEqual(expected_winner, actual_winner)

        expected_loser = self.game.omega
        actual_loser = self.game.loser
        self.assertEqual(expected_loser, actual_loser)

    def test_omega_win(self):
        self.game.status = Status.COMPLETE
        self.game.alpha_score = 11
        self.game.omega_score = 13
        self.game.update_teams()

        expected_winner = self.game.omega
        actual_winner = self.game.winner
        self.assertEqual(expected_winner, actual_winner)

        expected_loser = self.game.alpha
        actual_loser = self.game.loser
        self.assertEqual(expected_loser, actual_loser)

    def test_not_started(self):
        self.game.status = Status.NOT_STARTED
        self.game.alpha_score = 0
        self.game.omega_score = 0
        self.game.update_teams()

        expected_winner = None
        actual_winner = self.game.winner
        self.assertEqual(expected_winner, actual_winner)

        expected_loser = None
        actual_loser = self.game.loser
        self.assertEqual(expected_loser, actual_loser)

    def test_in_progress(self):
        self.game.status = Status.IN_PROGRESS
        self.game.alpha_score = 6
        self.game.omega_score = 6
        self.game.update_teams()

        expected_winner = None
        actual_winner = self.game.winner
        self.assertEqual(expected_winner, actual_winner)

        expected_loser = None
        actual_loser = self.game.loser
        self.assertEqual(expected_loser, actual_loser)


if __name__ == '__main__':
    unittest.main()
