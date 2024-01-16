import unittest
from unittest.mock import Mock
from server.time.TimeController import TimeController
from api.j2l.pytactx.agent import Agent

class TimeControllerTest(unittest.TestCase):

    def setUp(self):
        self.mock_agent = Mock(spec=Agent)
        self.time_controller = TimeController(self.mock_agent)

    def test_start(self):
        """Test the start method."""
        self.time_controller.start()
        self.assertIsNotNone(self.time_controller._TimeController__start_timestamp)

    def test_startLap(self):
        """Test the startLap method."""
        self.time_controller.startLap()
        self.assertIsNotNone(self.time_controller._TimeController__start_lap_timestamp)

    def test_stopLap(self):
        """Test the stopLap method."""
        self.time_controller.startLap()
        self.mock_agent.game = {"t": 1000}
        self.time_controller.stopLap()

        # Ensure remaining lap time is updated
        self.assertIsNotNone(self.time_controller._TimeController__remaining_lap_time)

    def test_setBestLapTime(self):
        """Test the setBestLapTime method."""
        player_id = 1
        lap_time = 2000
        self.time_controller.setBestLapTime(player_id, lap_time)
        self.assertEqual(self.time_controller._TimeController__best_lap_times[player_id], lap_time)

    def test_getBestLapTime(self):
        """Test the getBestLapTime method."""
        player_id = 1
        lap_time = 2000
        self.time_controller.setBestLapTime(player_id, lap_time)
        self.assertEqual(self.time_controller.getBestLapTime(), lap_time)

    def test_getRoundDuration(self):
        """Test the getRoundDuration method."""
        self.assertEqual(self.time_controller.getRoundDuration(), 300)

    def test_setRoundDuration(self):
        """Test the setRoundDuration method."""
        self.time_controller.setRoundDuration(400)
        self.assertEqual(self.time_controller.getRoundDuration(), 400)

    def test_getWarmUpDuration(self):
        """Test the getWarmUpDuration method."""
        self.assertEqual(self.time_controller.getWarmUpDuration(), 60)

    def test_setWarmUpDuration(self):
        """Test the setWarmUpDuration method."""
        self.time_controller.setWarmUpDuration(90)
        self.assertEqual(self.time_controller.getWarmUpDuration(), 90)

    def test_getLapDuration(self):
        """Test the getLapDuration method."""
        self.assertEqual(self.time_controller.getLapDuration(), 30)

    def test_setLapDuration(self):
        """Test the setLapDuration method."""
        self.time_controller.setLapDuration(40)
        self.assertEqual(self.time_controller.getLapDuration(), 40)

    def test_getCurrTimestamp(self):
        """Test the getCurrTimestamp method."""
        self.mock_agent.game = {"t": 1500}
        self.assertEqual(self.time_controller.getCurrTimestamp(), 1500)

    def test_getRemainingTime(self):
        """Test the getRemainingTime method."""
        self.mock_agent.game = {"t": 2000}
        self.time_controller.start()
        self.assertEqual(self.time_controller.getRemainingTime(), 100)

    def test_setRemainingTime(self):
        """Test the setRemainingTime method."""
        self.mock_agent.game = {"t": 2500}
        self.time_controller.start()
        self.time_controller.setRemainingTime()
        self.assertEqual(self.time_controller._TimeController__remaining_time, 50)

    def test_getRemainingLapTime(self):
        """Test the getRemainingLapTime method."""
        self.time_controller.startLap()
        self.mock_agent.game = {"t": 3000}
        self.assertEqual(self.time_controller.getRemainingLapTime(), 27.0)

    def test_format_time(self):
        """Test the format_time method."""
        formatted_time = self.time_controller.format_time(75000)
        self.assertEqual(formatted_time, "01:15.000")

if __name__ == '__main__':
    unittest.main()
