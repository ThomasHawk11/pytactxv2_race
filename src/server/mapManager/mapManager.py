from __future__ import annotations
import random
from typing import TypeAlias
import j2l.pytactx.agent as pytactx
import time

CollisionMatrix: TypeAlias = list[list[int]]
Agent: TypeAlias = pytactx.Agent
Friction: TypeAlias = list[int]
MapImgs: TypeAlias = list[str]
Checkpoints: TypeAlias = list[dict]


class Map:

  def __init__(self, url: str, collisionMatrix: CollisionMatrix, rows: int,
               cols: int, friction: Friction, mapImgs: MapImgs,
               checkpoints: Checkpoints):
    self.collisionMatrix = None
    self.url = None
    self.size = {"rows": None, "cols": None}
    self.friction = None
    self.mapImgs = None
    self.checkpoints = None

    self.setSize(rows, cols)
    self.setUrl(url)
    self.setCollisionMatrix(collisionMatrix)
    self.setFriction(friction)
    self.setMapImgs(mapImgs)
    self.setCheckpoints(checkpoints)

  def getUrl(self) -> str:
    return self.url

  def setUrl(self, url: str) -> bool:
    if (url != None and isinstance(url, str)):
      self.url = url
      return True
    return False

  def getCollisionMatrix(self) -> CollisionMatrix:
    return self.collisionMatrix

  def setCollisionMatrix(self, collisionMatrix: CollisionMatrix) -> bool:
    if (collisionMatrix != None and isinstance(collisionMatrix, list)):
      for i in range(0, len(collisionMatrix)):
        if (isinstance(collisionMatrix[i], list) == False):
          return False
        for j in range(0, len(collisionMatrix[i])):
          if (isinstance(collisionMatrix[i][j], int) == False):
            return False
      self.collisionMatrix = collisionMatrix
      return True
    return False

  def getSize(self) -> dict:
    return self.size

  def setSize(self, rows: int, cols: int) -> bool:
    if (rows != None and cols != None and isinstance(rows, int) and rows >= 0
        and isinstance(cols, int) and cols >= 0):
      self.size["rows"] = rows
      self.size["cols"] = cols
      return True
    return False

  def getFriction(self) -> Friction:
    return self.friction

  def setFriction(self, friction: Friction) -> bool:
    if (friction != None and isinstance(friction, list)):
      for i in range(0, len(friction)):
        if (isinstance(friction[i], int) == False
            and isinstance(friction[i], float) == False):
          return False
      self.friction = friction
      return True
    return False

  def getMapImgs(self) -> MapImgs:
    return self.mapImgs

  def setMapImgs(self, mapImgs: MapImgs) -> bool:
    if (mapImgs != None and isinstance(mapImgs, list)):
      for i in range(0, len(mapImgs)):
        if (isinstance(mapImgs[i], str) == False):
          return False
      self.mapImgs = mapImgs
      return True
    return False

  def getCheckpoints(self) -> Checkpoints:
    return self.checkpoints

  def setCheckpoints(self, checkpoints: Checkpoints) -> bool:
    if (checkpoints != None and isinstance(checkpoints, list)):
      for i in range(0, len(checkpoints)):
        if (isinstance(checkpoints[i], dict) == False
            or checkpoints[i]["x"] == None or checkpoints[i]["y"] == None
            or isinstance(checkpoints[i]["x"], int) == False
            or isinstance(checkpoints[i]["y"], int) == False):
          print("erreur")
          return False
      self.checkpoints = checkpoints
      return True


Maps: TypeAlias = list[Map]


class MapPool:
  __mapPoolInstance = None

  def __init__(self):
    self.maps = []

  @staticmethod
  def getInstance() -> MapPool:
    if (MapPool.__mapPoolInstance == None):
      MapPool.__mapPoolInstance = MapPool()
    return MapPool.__mapPoolInstance

  def getMaps(self) -> Maps:
    return self.maps

  def getMapByIdx(self, idx: int) -> Map:
    if (idx != None and isinstance(idx, int) and idx >= 0
        and idx < len(self.maps)):
      return self.maps[idx]

  def getRandomMap(self) -> Map:
    mapsMaxIdx = len(self.maps) - 1
    if (mapsMaxIdx >= 0):
      return self.maps[random.randint(0, mapsMaxIdx)]
    return None

  def addMap(self, map: Map) -> bool:
    if (map != None and isinstance(map, Map)):
      self.getMaps().append(map)
      return True
    return False


class MapManager:
  __mapInstance = None

  def __init__(self):
    self.agent = None

  @staticmethod
  def getInstance() -> MapManager:
    if (MapManager.__mapInstance == None):
      MapManager.__mapInstance = MapManager()
    return MapManager.__mapInstance

  def setAgent(self, agentToSet: Agent) -> bool:
    if agentToSet != None and isinstance(agentToSet, Agent):
      self.agent = agentToSet
      return True
    return False

  def getAgent(self) -> Agent:
    return self.agent

  def setMap(self, map: Map) -> bool:
    if (map != None and isinstance(map, Map) and self.agent != None
        and isinstance(self.agent, Agent)):
      if (map.getSize() != None and map.getSize()["rows"] != None
          and map.getSize()["cols"] != None
          and isinstance(map.getSize()["rows"], int)
          and isinstance(map.getSize()["cols"], int)):
        self.agent.ruleArena("gridColumns", map.getSize()["cols"])
        self.agent.ruleArena("gridRows", map.getSize()["rows"])
        time.sleep(1)
        self.agent.update()
        if (map.getCollisionMatrix() != None):
          self.agent.ruleArena("map", map.getCollisionMatrix())

      if (map.getUrl() != None):
        self.agent.ruleArena("bgImg", map.getUrl())

      if (map.getFriction() != None):
        self.agent.ruleArena("mapFriction", map.getFriction())

      if (map.getMapImgs() != None):
        self.agent.ruleArena("mapImgs", map.getMapImgs())

      if (map.getCheckpoints() != None):
        self.agent.ruleArena("dtFire", map.getCheckpoints())

      self.agent.update()
      return True

    return False
