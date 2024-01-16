from __future__ import annotations
import random
from typing import TypeAlias
import j2l.pytactx.agent as pytactx
import time

Agent: TypeAlias = pytactx.Agent


class RuleManager:
  __mapInstance = None

  def __init__(self):
    self.agent = None

  @staticmethod
  def getInstance() -> RuleManager:
    if (RuleManager.__mapInstance == None):
      RuleManager.__mapInstance = RuleManager()
    return RuleManager.__mapInstance

  def setAgent(self, agentToSet: Agent) -> bool:
    if agentToSet != None and isinstance(agentToSet, Agent):
      self.agent = agentToSet
      return True
    return False

  def getAgent(self) -> Agent:
    return self.agent

  def setupGameRules(self) -> bool:
    agent = self.getAgent()
    if agent != None and isinstance(agent, Agent):
      rules = [["invisible", [False, False, False, False, False]],
               ["spawnArea", {
                 "x": [28],
                 "y": [17],
                 "r": [0]
               }], ["nRespawn", [0, 0, 0, 0, 1]], ["borderHit", 0],
               ["collision", [False, False, False, False, False]],
               ["PImgs",[
                 "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/vehicule.svg",
                 "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/vehicule.svg",
                 "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/vehicule.svg",
                 "rocket.svg"
               ],
               ["invicible", [True, True, True, True, True]],
               ["accelerationOnly", [True, True, True, True, True]],
               ["dtMove", [1, 1, 1, 1, 1]], ["dtDir", [1, 1, 1, 1, 1]],
               ["moveToDir", [True, True, True, True, True]],
               ["dDirMax", [40, 30, 30, 30, 30]],
               ["fxFire", [False, False, False, False, False]],
               ["hitCollision", [0, 1, 0, 0, 0]],
               ["range", [0 for i in range(5)]]]
      for rule in rules:
        agent.ruleArena(rule[0], rule[1])
        time.sleep(0.2)
      agent.update()
      return True
    return False
