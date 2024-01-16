import os
from dotenv import load_dotenv
import gameLoop
import time
import j2l.pytactx.agent as pytactx

load_dotenv()

# Create the agent
agent = pytactx.Agent(playerId=os.getenv("PLAYERID"),
	arena=os.getenv("ARENA"),
	username=os.getenv("USERNAME"),
	password=os.getenv("PASSWORD"),
	server=os.getenv("SERVER"),
	verbosity=2)

# The gameloop
cls = gameLoop.GameLoop(agent)
while True:
	cls.next()
	time.sleep(1.5)
	agent.update()
