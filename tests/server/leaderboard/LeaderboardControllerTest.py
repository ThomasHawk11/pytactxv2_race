import unittest
from unittest.mock import Mock
from server.time.TimeController import TimeController
from server.leaderboard.LeaderboardController import LeaderboardController
from api.j2l.pytactx.agent import Agent

class TestLeaderboardController(unittest.TestCase):

  def setUp(self):
    self.mock_arbitre = Mock(spec=Agent)
    self.mock_time_controller = Mock(spec=TimeController)
    self.leaderboard_controller = LeaderboardController(self.mock_arbitre, self.mock_time_controller)

  def test_updateLeaderboard(self):
    """
    Test the updateLeaderboard method.
    :param self: The test object.
    :type self: object
    """
    best_lap_times = {'player1': 10.5, 'player2': 12.3, 'player3': 9.8}
    self.mock_time_controller.getBestLapTimes.return_value = best_lap_times

    self.leaderboard_controller.updateLeaderboard()

    self.assertIsNotNone(self.leaderboard_controller.getHighscore())
    self.assertIsNotNone(self.leaderboard_controller.getLeaderboard())

    sorted_lap_times = sorted(best_lap_times.values())
    self.assertEqual(list(best_lap_times.values()), sorted_lap_times)

    
  def test_getRank(self):
    """
    Test the getRank method.
    :param self: The test object.
    :type self: object
    """
    best_lap_times = {'player1': 10.5, 'player2': 12.3, 'player3': 9.8}
    self.mock_time_controller.getBestLapTimes.return_value = best_lap_times

    rank = self.leaderboard_controller.getRank('player2')

    self.assertEqual(rank, 2)

  def test_setHighscore(self):
    """
    Test the setHighscore method.
    :param self: The test object.
    :type self: object
    """
    highscore_tuple = ('player1', 9.5, 1)
    self.leaderboard_controller.setHighscore(highscore_tuple)

    highscore = self.leaderboard_controller.getHighscore()
    self.assertIsNotNone(highscore)
    self.assertEqual(highscore['player_id'], 'player1')
    self.assertEqual(highscore['lap_time'], 9.5)
    self.assertEqual(highscore['rank'], 1)

if __name__ == '__main__':
    unittest.main()