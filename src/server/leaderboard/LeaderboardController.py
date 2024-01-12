import api.j2l.pytactx.agent as pytactx
import server.time.TimeController as timectrl
from typing import List, Tuple
from operator import itemgetter

class ILeaderboardController:
  def updateLeaderboard(self) -> None:
    """
    Update the leaderboard and set highscore if needed.
    """
  def showLeaderboard(self, player: pytactx.Agent) -> None:
    """
    Show the leaderboard.
  
    :param player: the player agent
    :type player: Agent
    """
  def setHighscore(self, highscore: Tuple) -> None:
    """
    Set highscore using best lap time.

    :param highscore: Tuple containing information about the highscore
    :type highscore: Tuple
    """
  def getRank(self, player_id: str) -> int:
    """
    Get the rank of a player based on their best lap time.

    :param player_id: The ID of the player.
    :type player_id: str
    :return: The rank of the player.
    :rtype: int
    """
  def getHighscore(self):
    """
    Get highscore.
    """
  def getLeaderboard(self) -> List:
    """
    Get the leaderboard.   

    :return: List containing information about the leaderboard
    :rtype: List
    """
  def setLeaderboard(self, leaderboard: List) -> None:
    """
    Set the leaderboard.

    :param leaderboard: List containing information about the leaderboard
    :type leaderboard: List
    """
  def getArbitre(self):
    """
    Get the referee.

    :return: The referee agent
    :rtype: Agent
    """
  

class LeaderboardController(ILeaderboardController):
  def __init__(self, arbitre: pytactx.Agent, time_controller: timectrl.TimeController) -> None:
    """
    Initialize the leaderboard.

    :param arbitre: the game referee agent
    :type arbitre: Agent
    :param time_controller: the time controller instance
    :type time_controller: TimeController
    """
    self.__arbitre = arbitre
    self.__time_controller = time_controller
    self.__arbitre.ruleArena("info", "⌛ Initialisation du classement...")
    self.__leaderboard = []
    self.__highscore = None

  def updateLeaderboard(self) -> None:
    """
    Update the leaderboard and set highscore if needed.
    """
    self.__arbitre.ruleArena("info", "⌛ Mise à jour du du classement...")
    best_lap_times = self.__time_controller.getBestLapTimes()
    
    player_info_list = []
    for player_id, lap_time in best_lap_times.items():
        player_info = {
            'player_id': player_id,
            'lap_time': lap_time,
            'rank': self.getRank(player_id),
        }
        player_info_list.append(player_info)
    
    player_info_list.sort(key=itemgetter('lap_time'))
    
    if not self.__highscore or player_info_list[0]['lap_time'] < self.__highscore['lap_time']:
        self.__highscore = {
            'player_id': player_info_list[0]['player_id'],
            'lap_time': player_info_list[0]['lap_time'],
            'rank': player_info_list[0]['rank'],
        }
    
    self.__leaderboard = player_info_list

  def showLeaderboard(self) -> None:
    """
    Show the leaderboard.

    :param player: the player agent
    :type player: Agent
    """
    self.__arbitre.ruleArena("info", "🏆 High score : {} - {} s".format(self.__highscore['player_id'], self.__highscore['lap_time']))

  def setHighscore(self, highscore: Tuple) -> None:
    """
    Set highscore using best lap time.

    :param highscore: Tuple containing information about the highscore
    :type highscore: Tuple
    """
    self.__highscore = highscore

  def getRank(self, player_id: str) -> int:
    """
    Get the rank of a player based on their best lap time.

    :param player_id: The ID of the player.
    :type player_id: str
    :return: The rank of the player.
    :rtype: int
    """
    best_lap_times = self.__time_controller.getBestLapTimes()

    player_info_list = []
    for pid, lap_time in best_lap_times.items():
        player_info = {
            'player_id': pid,
            'lap_time': lap_time,
        }
        player_info_list.append(player_info)

    player_info_list.sort(key=itemgetter('lap_time'))

    for idx, info in enumerate(player_info_list):
        if info['player_id'] == player_id:
            return idx + 1 

    return -1

  def getHighscore(self):
    """
    Get highscore.
    """
    return self.__highscore

  def getLeaderboard(self) -> List:
    """
    Get the leaderboard.

    :return: List containing information about the leaderboard
    :rtype: List
    """
    return self.__leaderboard

  def setLeaderboard(self, leaderboard: List) -> None:
    """
    Set the leaderboard.

    :param leaderboard: List containing information about the leaderboard
    :type leaderboard: List
    """
    self.__leaderboard = leaderboard

  def getArbitre(self):
    """
    Get the referee.

    :return: The referee agent
    :rtype: Agent
    """
    return self.__arbitre





  
