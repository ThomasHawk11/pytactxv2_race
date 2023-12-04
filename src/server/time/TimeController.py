from api.j2l.pytactx.agent import Agent
from datetime import timedelta

class TimeController:

    def start(self) -> None:
        """Start the time master, saving the current timestamp."""

    def getRoundDuration(self) -> int:
        """Return the round duration."""

    def setRoundDuration(self, timer: int) -> None:
        """Set the round duration, in seconds."""

    def getWarmUpDuration(self) -> int:
        """Return the warm-up duration."""
        
    def setWarmUpDuration(self, timer: int) -> None:
        """Set the warm-up duration, in seconds."""

    def getLapDuration(self) -> int:
        """Return the lap duration."""

    def setLapDuration(self, timer: int) -> None:
        """Set the lap duration, in seconds."""

    def startLap(self) -> None:
        """Start the lap timer, saving the current timestamp."""

    def stopLap(self) -> None:
        """Stop the lap timer."""

    def getCurrTimestamp(self) -> int:
        """Return the current timestamp from the server."""

    def getRemainingTime(self) -> int:
        """Return remaining time based on the startTimestamp and the currTimestamp."""

    def setRemainingTime(self) -> None:
        """Set the remaining time depending on the elapsed time."""

class TimeController(TimeController):
    def __init__(self,
                 agent: Agent,
                 round_duration: int = 300,
                 warm_up_duration: int = 60,
                 lap_duration: int = 30) -> None:
        """
        Initialize TimeController instance.

        :param agent: The game agent.
        :param round_duration: The duration of a round in seconds.
        :param warm_up_duration: The duration of warm-up in seconds.
        :param lap_duration: The duration of a lap in seconds.
        """
        self.__pytactx_agent = agent
        self.__round_duration = round_duration
        self.__warm_up_duration = warm_up_duration
        self.__lap_duration = lap_duration
        self.__start_timestamp = None
        self.__start_lap_timestamp = None
        self.__remaining_time = None
        self.__remaining_lap_time = None
        self.__best_lap_time = float('inf')  # Initialise avec un positif infini

    def start(self) -> None:
        """Start the time master, saving the current timestamp."""
        self.__start_timestamp = self.__pytactx_agent.game["t"]

    def startLap(self) -> None:
        """Start the lap timer, saving the current timestamp."""
        self.__start_lap_timestamp = self.__pytactx_agent.game["t"]

    def stopLap(self) -> None:
        """Stop the lap timer and update the best lap time if needed."""
        elapsed_time = self.__pytactx_agent.game["t"] - self.__start_lap_timestamp
        self.__remaining_lap_time = elapsed_time
        if elapsed_time < self.__best_lap_time:
            self.__best_lap_time = elapsed_time

    def getBestLapTime(self) -> int:
        """Return the best lap time."""
        return self.__best_lap_time

    def getRoundDuration(self) -> int:
        return self.__round_duration

    def setRoundDuration(self, timer: int) -> None:
        if timer < 0:
            return "Il faut un entier positif"
        self.__round_duration = timer

    def getWarmUpDuration(self) -> int:
        return self.__warm_up_duration

    def setWarmUpDuration(self, timer: int) -> None:
        if timer < 0:
            return "Il faut un entier positif"
        self.__warm_up_duration = timer

    def getLapDuration(self) -> int:
        return self.__lap_duration

    def setLapDuration(self, timer: int) -> None:
        if timer < 0:
            return "Il faut un entier positif"
        self.__lap_duration = timer

    def getCurrTimestamp(self) -> int:
        return self.__pytactx_agent.game["t"]

    def getRemainingTime(self) -> int:
        self.setRemainingTime()
        return self.__remaining_time

    def setRemainingTime(self) -> None:
        delta_time = (self.getCurrTimestamp() - self.__start_timestamp) / 1000
        self.__remaining_time = max(0, self.__round_duration - delta_time)

    def getRemainingLapTime(self) -> int:
        return self.__lap_duration - (self.__remaining_lap_time / 1000)

    def format_time(self, milliseconds: int) -> str:
      """
      Format the given time duration in milliseconds into a human-readable string.

      :param milliseconds: The time duration in milliseconds.
      :return: A formatted string representing the time.
      """
      duration = timedelta(milliseconds=milliseconds)
      minutes, seconds = divmod(duration.seconds, 60)
      return f"{minutes:02d}:{seconds:02d}.{int(duration.microseconds / 1000):03d}"
