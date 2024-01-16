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
      agent.ruleArena("range", [0 for i in range(5)])
      agent.ruleArena("invisible", [False, False, False, False, False])
      time.sleep(0.5)

      agent.ruleArena("spawnArea", {"x": [28], "y": [17], "r": [0]})
      agent.ruleArena("nRespawn", [0, 0, 0, 0, 1])
      agent.ruleArena("borderHit", 0)
      agent.ruleArena("collision", [False, False, False, False, False])
      time.sleep(0.5)

      agent.ruleArena("invicible", [True, True, True, True, True])
      agent.ruleArena("accelerationOnly", [True, True, True, True, True])
      agent.ruleArena("accelerationOnly", [True, True, True, True, True])
      time.sleep(0.5)

      agent.ruleArena("dtMove", [1, 1, 1, 1, 1])

      agent.ruleArena("dtDir", [1, 1, 1, 1, 1])

      agent.ruleArena("moveToDir", [True, True, True, True, True])
      agent.ruleArena("dDirMax", [30, 30, 30, 30, 30])

      agent.ruleArena("fxFire", [False, False, False, False, False])
      agent.ruleArena("hitCollision", [0, 0, 0, 0, 0])

      agent.update()
      return True
    return False