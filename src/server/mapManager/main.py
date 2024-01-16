from mapManager import *
import j2l.pytactx.agent as pytactx
from ../rulesManager/rulesManager import *

def main():
  agent = pytactx.Agent(playerId="02102003",
    arena="turbovroum",
    username="demo",
    password="demo",
    server="mqtt.jusdeliens.com",
    verbosity=2)
  mapPool = MapPool.getInstance()
  ruleManager = RuleManager.getInstance()
  ruleManager.setAgent(agent)
  mapManager = MapManager.getInstance()
  mapManager.setAgent(agent)
    
  mapPool.addMap(
    Map(
      url=
      "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/race.png",
      rows=35,
      cols=50,
      collisionMatrix=[[
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1
      ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                         2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                         2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0,
                         0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 0, 0,
                         0, 0, 0, 0, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0,
                         0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 2, 2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 2, 2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 1
                       ],
                       [
                         1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2,
                         2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1
                       ],
                       [
                         1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1,
                         1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         2, 2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 2, 1
                       ],
                       [
                         1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
                         2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 2, 1
                       ],
                       [
                         1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 2, 1
                       ],
                       [
                         1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
                         1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
                         2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
                         2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                         2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0,
                         0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0,
                         0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0,
                         0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0,
                         0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0,
                         0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0,
                         2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2,
                         2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1
                       ],
                       [
                         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1
                       ],
                       [
                         1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1
                       ],
                       [
                         1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1
                       ],
                       [
                         1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                         0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1
                       ],
                       [
                         1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                         2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1
                       ],
                       [
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                       ]],
      friction=[0, 1, 0.4],
      mapImgs=[
        "",
        "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/colision_1.png",
        "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/colision_2.png"
      ],
      checkpoints=[{
        "x": 28,
        "y": 17
      }, {
        "x": 7,
        "y": 31
      }, {
        "x": 16,
        "y": 8
      }, {
        "x": 42,
        "y": 3
      }, {
        "x": 38,
        "y": 41
      }]))
  mapPool.addMap(
    Map(
      url=
      "https://raw.githubusercontent.com/ThomasHawk11/pytactxv2_race/main/res/race.png",
      rows=25,
      cols=40,
      collisionMatrix=[[0, 0, 0, 0, 0, 0, 0]],
      friction=[0, 0, 0],
      mapImgs=["", ""],
      checkpoints=[{
        "x": 0,
        "y": 0
      }, {
        "x": 10,
        "y": 10
      }]))

  mapManager.setMap(mapPool.getMapByIdx(0))
  ruleManager.setupGameRules();

main()
