from typing import Any
from api.j2l.pytactx.agent import Agent

class TimeController:

  def start(self) -> None:
    """
        Start the time master, saving the current timestamp
        """

  def getRoundDuration(self) -> int:
    """
        Return the round duration
        """
    
  def setRoundDuration(self, timer: int) -> None:
    """
        Set the round duration, in seconds
        """

  def getWarmUpDuration(self) -> int:
    """
        Return the warm-up duration
        """

  def setWarmUpDuration(self, timer: int) -> None:
    """
        Set the warm-up duration, in seconds
        """

  def getLapDuration(self) -> int:
    """
        Return the lap duration
        """

  def setLapDuration(self, timer: int) -> None:
    """
        Set the lap duration, in seconds
        """

  def startLap(self) -> None:
    """
        Start the lap timer, saving the current timestamp
        """

  def stopLap(self) -> None:
    """
        Stop the lap timer
        """

  def getCurrTimestamp(self) -> int:
    """
        Return the current timestamp from the server
        """

  def getRemainingTime(self) -> int:
    """
        Return remaining time based on the startTimestamp and the currTimestamp
        """

  def setRemainingTime(self) -> None:
    """
        Set the remaining time depending on the elapsed time
        """

class TimeController(TimeController):
  def __init__(self,
               agent: Agent,
               round_duration: int = 300,
               warm_up_duration: int = 60,
               lap_duration: int = 30) -> None:
    self.__pytactxAgent = agent
    self.__roundDuration = round_duration
    self.__warmUpDuration = warm_up_duration
    self.__lapDuration = lap_duration
    self.__startTimestamp = None
    self.__startLapTimestamp = None
    self.__remainingTime = None
    self.__remainingLapTime = None

  def start(self) -> None:
    self.__startTimestamp = self.__pytactxAgent.game["t"]

  def getRoundDuration(self) -> int:
    return self.__roundDuration

  def setRoundDuration(self, timer: int) -> Any:
    if timer < 0:
      return "Il faut un entier positif"
    self.__roundDuration = timer
    return self.__roundDuration

  def getWarmUpDuration(self) -> int:
    return self.__warmUpDuration

  def setWarmUpDuration(self, timer: int) -> Any:
    if timer < 0:
      return "Il faut un entier positif"
    self.__warmUpDuration = timer
    return self.__warmUpDuration

  def getLapDuration(self) -> int:
    return self.__lapDuration

  def setLapDuration(self, timer: int) -> Any:
    if timer < 0:
      return "Il faut un entier positif"
    self.__lapDuration = timer
    return self.__lapDuration

  def startLap(self) -> None:
    self.__startLapTimestamp = self.__pytactxAgent.game["t"]

  def stopLap(self) -> None:
    self.__remainingLapTime = self.__pytactxAgent.game[
      "t"] - self.__startLapTimestamp

  def getCurrTimestamp(self) -> int:
    return self.__pytactxAgent.game["t"]

  def getRemainingTime(self) -> int:
    self.setRemainingTime()
    return self.__remainingTime

  def setRemainingTime(self) -> None:
    delta_time = (self.getCurrTimestamp() - self.__startTimestamp) // 1000
    self.__remainingTime = max(0, self.__roundDuration - delta_time)

  def getRemainingLapTime(self) -> int:
    return self.__lapDuration - (self.__remainingLapTime // 1000)
