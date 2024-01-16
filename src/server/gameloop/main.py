import gameLoop
import time
import j2l.pytactx.agent as pytactx

# Create the agent
agent = pytactx.Agent(playerId=input("gameloop manager login : "),
                      arena="turbovroum",
                      username="demo",
                      password="demo",
                      server="mqtt.jusdeliens.com",
                      verbosity=2)

# The gameloop
cls = gameLoop.GameLoop(agent)
while True:
	cls.next()
	time.sleep(1.5)
	agent.update()
